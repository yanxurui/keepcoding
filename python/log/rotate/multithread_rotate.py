# the same with multiple processes
import os
import stat
import logging
import logging.handlers
from multiprocessing.pool import Pool

logger = logging.getLogger(__name__)
fh = logging.handlers.RotatingFileHandler('spam.log', maxBytes=100, backupCount=5)
logger.addHandler(fh)

def log(id):
    print id
    for i in range(2000):
        logger.error('I am %d#%d' % (id, i))
        ino = os.fstat(fh.stream.fileno())[stat.ST_INO]
        try:
            sres = os.stat('spam.log')
        except OSError as err:
            if err.errno == errno.ENOENT:
                sres = None
            else:
                raise
        if sres:
            assert sres[stat.ST_INO] == ino

# threading pool: https://stackoverflow.com/a/3386632/6088837
p = Pool(10)
p.map(log, range(10))
