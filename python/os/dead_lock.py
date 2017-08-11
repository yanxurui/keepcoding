#!/usr/bin/env
# coding=utf-8

import threading

lock = threading.Lock()

def run1():
    """for Thread-1
    
    aborted thread will not release lock
    """
    lock.acquire()
    print(1+'1')
    lock.release()

def run2():
    lock.acquire()
    print(1+1)
    lock.release()


def main():
    t1 = threading.Thread(target=run1)
    t2 = threading.Thread(target=run2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
