# create self-signed certificate
# openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.key
# openssl x509 -text -noout -in cert.pem

# look at <https://stackoverflow.com/questions/10175812/how-to-create-a-self-signed-certificate-with-openssl> for details

import socket, ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='cert.key')

bindsocket = socket.socket()
bindsocket.bind(('mononoke.com', 4433))
bindsocket.listen(5)


def echo(connstream):
    while True:
        data = connstream.read()
        if not data:
            print('null data means the client is finished with us')
            break
        if data == 'q':
            print('client quit')
            break
        connstream.sendall(data)
    # finished with client

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        echo(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()
