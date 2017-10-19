#!/usr/bin/env
# coding=utf-8

import pdb

def answer0(start, length):
    def gen(start, length):
        for i in range(length):
            for j in range(length - i):
                yield start
                start += 1
            start += i
                
    result = 0
    for i in gen(start, length):
        result = result ^ i
    return result

# compute xor from 1 to n
# n >= 0
def xor(n):
    result = n
    for i in range(1,n):
        result = result^i
    return result

# 算法原理
# http://www.cnblogs.com/flyinghearts/archive/2011/03/22/1992001.html
def xor_n(n):
    r = n % 4
    if r== 0:
        return n
    if r==1:
        return 1
    if r==2:
        return n+1
    if r==3:
        return 0

def xor_n(n):
    return [n,1,n+1,0][n % 4]

def xor_m_n(m,n):
    assert n>m>=0
    return xor_n(m)^xor_n(n)

def answer(start, length):
    temp = []
    i=0
    if start==0:
        temp.append(xor_n(length-1))
        i += 1
    while i<length:
        temp.append(xor_m_n(start-1+i*length, start-1+i*length+length-i))
        i += 1
    result = 0
    for i in temp:
        result = result ^ i
    return result



if __name__ == '__main__':
    from test_func import test
    test(answer0,
        [
            ((1,2), 0),
            ((2,1), 2),
            ((0,3), 2),
            ((17,4), 14),
            # ((0, 10000), 82460672),
            # ((0, 50000), 2364908544),
        ])
    test(answer,
        [
            ((1,2), 0),
            ((2,1), 2),
            ((0,3), 2),
            ((17,4), 14),
            ((0, 10000), 82460672),
            ((0, 50000), 2364908544),
        ])


    test(xor_n,
        [
            (3, xor(3)),
            (10, xor(10)),
            (20, xor(20)),
            (10000, xor(10000)),
        ])
