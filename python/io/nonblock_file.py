# there is no way to write to a file asynchronously on Linux or on Windows
# https://stackoverflow.com/a/13644499/6088837

import os
import datetime

data = 'x'*700000000
print("Size of data is %d bytes" % len(data))

print("open at %s" % str(datetime.datetime.now()))
fd = os.open("filename", os.O_CREAT | os.O_WRONLY | os.O_NONBLOCK)
print("write at %s" % str(datetime.datetime.now()))
os.write(fd, data)
print("close at %s" % str(datetime.datetime.now()))
os.close(fd)
print("end at %s" % str(datetime.datetime.now()))
