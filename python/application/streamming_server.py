import re
import logging

import asyncio
from aiohttp import web

streams = []
logging.basicConfig(format='%(asctime)s %(levelname)s %(filename)s:%(lineno)d: %(message)s',level=logging.INFO)

class Stream:
    def __init__(self, s_id):
        self.id = s_id
        self.flv_header = None
        self.meta_header = None # scriptData, AVC/AAC sequence header
        self.queue_size = 1000 # around 10MB for 720p
        self.tag_id = 0
        self.tags_queue = [None]*self.queue_size
        self.alive = False
        self.players = []
        self.condition = asyncio.Condition()

    def __repr__(self):
        return 'stream:%d' % self.id

    @property
    def player_num(self):
        return len(list(filter(lambda x:bool(x), self.players)))

    def end(self):
        # destroy the buffer when publish ended and number of players drops to 0
        if not self.alive and self.player_num == 0:
            logging.info('%s destroy the buffer' % self)
            del self.tags_queue

    async def push(self, reader):
        logging.info('push %s' % self)
        self.flv_header = await reader.read(9+4) # includes the size of tag 0
        # Converting int to bytes in Python 3: https://stackoverflow.com/a/21017834/6088837
        if self.flv_header != b'FLV'+bytes([1,5,0,0,0,9,0,0,0,0]):
            logging.warning('stream is not flv')
            return
        while True:
            tag_header = await reader.read(11)
            if not tag_header: # eof
                break
            tag_size = int.from_bytes(tag_header[1:4], byteorder='big')
            tag_body = await reader.read(tag_size+4) # include the size of this tag
            tag = tag_header + tag_body
            logging.debug('%s receive tag:%d' % (self, self.tag_id))
            self.tags_queue[self.tag_id%self.queue_size] = tag
            # video/audio header sequence contains codec information needed by
            # the decoder to be able to interpret the rest of the data
            if not self.meta_header:
                if (
                    # Video tag not AVC sequence header
                    ((tag[0] & 0x1F == 9) and not ((tag[11] & 0x0F == 7) and (tag[12] == 0)))
                    or
                    # Audio tag not AAC sequence header
                    ((tag[0] & 0x1F == 8) and not ((((tag[11] & 0xF0) >> 4) == 10) and (tag[12] == 0)))
                ):
                    logging.info('%s first media tag at %d' % (self, self.tag_id))
                    self.meta_header = b''.join(self.tags_queue[:self.tag_id])
                    self.alive = True
            self.tag_id = self.tag_id + 1
            with await self.condition:
                self.condition.notify_all()
        logging.info('%s closed, %d tags received' % (self, self.tag_id))
        self.alive = False
        # in case some players are waiting next tag
        with await self.condition:
            self.condition.notify_all()
        self.end()

    async def pull(self, resp):
        player_id = len(self.players)
        player = 'player:%d' %  player_id
        self.players.append(True)
        resp.write(self.flv_header)
        resp.write(self.meta_header)
        find_key_frame = False
        offset = self.tag_id - 1
        logging.info('%s %s pull from offset %d' % (self, player, offset))
        while True:
            if offset == self.tag_id:
                if not self.alive:
                    self.players[player_id] = False
                    self.end()
                    return
                try:
                    await resp.drain() # send data here
                    if not self.alive:
                        # won't be notified anymore so don't wait
                        continue
                    logging.debug('%s %s wait for more tags' % (self, player))
                    with await self.condition:
                        await self.condition.wait()
                except asyncio.CancelledError:
                    logging.info('%s %s disconnected' % (self, player))
                    self.players[player_id] = False
                    self.end()
                    raise
                continue # important
                # continue
            elif offset < self.tag_id - self.queue_size:
                logging.info('%s %s is behind' % (self, player))
                offset = self.tag_id - 1
                continue
            # offset in [tag_id-queue_size, tag_id)
            tag = self.tags_queue[offset%self.queue_size]
            if not find_key_frame:
                # video tag and key frame
                if (tag[0] & 0x1F == 9 and (tag[11] & 0xF0) >> 4) == 1:
                    find_key_frame = True
                    logging.info('%s %s find keyframe tag:%d' % (self, player, offset))
                else:
                    offset = offset + 1
                    continue
            logging.debug('%s %s send tag:%d' % (self, player, offset))
            resp.write(tag)
            offset = offset + 1


async def handle_pull(request):
    m = re.search(r'/(\d+)', request.path)
    if m:
        stream_id = int(m.group(1))
        if stream_id < len(streams):
            stream = streams[stream_id]
            if stream.alive:
                resp = web.StreamResponse(headers={'Content-Type': 'video/x-flv', 'Connection': 'close', 'Cache_Control': 'no-cache'})
                if not (request.version[0] == 1 and request.version[1] == 0):
                    # mplayer use http1.0
                    # use chunked encoding for http1.1 and later
                    resp.enable_chunked_encoding()
                await resp.prepare(request) # sender headers
                await stream.pull(resp)
                return resp
    return web.Response(status=404, text='stream does not exit')

async def handle_push(reader, writer):
    """callback for client connected
    args: (StreamReader, StreamWriter)
    """
    stream = Stream(len(streams))
    streams.append(stream)
    await stream.push(reader)
    writer.close() # close socket

loop = asyncio.get_event_loop()

# stream server
tcp = loop.run_until_complete(asyncio.start_server(handle_push, '0.0.0.0', 8888, loop=loop))
# http server
server = web.Server(handle_pull)
http = loop.run_until_complete(loop.create_server(server, '0.0.0.0', 8080))

# Serve requests until Ctrl+C is pressed
logging.info('start...')
print('''
push address tcp://{}:{}
pull address http://{}:{}'''.format(*tcp.sockets[0].getsockname(), *http.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    logging.warning('stop...')
    pass

# Close the server
# close listening socket, current requests are still procedding
tcp.close()
loop.run_until_complete(tcp.wait_closed())

# loop.run_until_complete(server.shutdown()) # close transports
http.close()
loop.run_until_complete(http.wait_closed())

# cancel all pending tasks
tasks = asyncio.Task.all_tasks()
for task in tasks:
    task.cancel()
results = loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))

loop.close()
