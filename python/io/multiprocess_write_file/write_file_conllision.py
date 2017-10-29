#!/usr/bin/env
# coding=utf-8

import os
import sys
import time
from multiprocessing import Pool

def os_write():
    # fd = os.open('a.txt', os.O_WRONLY|os.O_APPEND)
    fd = os.open('a.txt', os.O_WRONLY)
    pid = os.getpid()
    print(pid)
    for i in range(10000):
        # time.sleep(0.001)
        os.write(fd, '%d:%d\n' % (pid, i))


def write():
    with open('a.txt', 'a') as f:
    # with open('a.txt', 'w') as f:
        pid = os.getpid()
        print(pid)
        for i in range(10000):
            # time.sleep(0.001)
            f.write('%d:%d\n' % (pid, i))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        p = Pool(n)
        for i in range(n):
            p.apply_async(write)
        p.close()
        p.join()
    else:
        print("Usage: %s process_num" % sys.argv[0])

# 结论
# 不同的进程写同一个文件
#   如果是append模式不会覆盖
#       如果是使用系统调用写文件，不会覆盖也不会交叉
#       如果使用应用程序级的write函数会导致行交叉
#   如果不是append
#       行会覆盖
