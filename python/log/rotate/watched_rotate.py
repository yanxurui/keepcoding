# work with logrotate

import logging
import logging.handlers
import time

logger = logging.getLogger(__name__)
# fh = logging.FileHandler('spam.log')
fh = logging.handlers.WatchedFileHandler('spam.log')
logger.addHandler(fh)

logger.error('something wrong') # (WARNING by default)
time.sleep(20) # mv spam.log to spam_old.log
logger.error('is it') # log to new file spam.log
