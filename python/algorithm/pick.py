#!/usr/bin/env
# coding=utf-8

#pick 3 balls from 3 box, how many combinations？
#balls in the same box are exactly the same
#two balls from different box are different from each other
def sub(a,b=0,c=0):
    count = 0
    if a+b+c<3:
        return 0
    for i in range(4):
        if i>a:
            continue
        for j in range(4-i):
            if j>b or 3-i-j>c:
                continue
            count=count+1
    return count
