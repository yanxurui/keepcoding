from __future__ import print_function
import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return tuple(map(int, sys.stdin.readline().split()))

########################
# greedy

def bi_search(array, b, e, x):
    # find the idx of the first value that is greater than x
    if b > e:
        return -1
    m = (b+e)/2
    if array[m] >= x:
        if m <=0 or array[m-1] < x:
            return m
        else:
            e = m - 1
    else:
        b = m + 1
    return bi_search(array, b, e, x)

def solver():
    D, S  = read_ints()
    res = []
    slots = []
    for s in range(S):
        slots.append(read_ints())
    # sort by e/c
    slots.sort(key=lambda (c,e): 1.0*e/c) # -1 unit coding => +c/e units eating
    coding = [slots[0][0]]
    eating = [sum([s[1] for s in slots])]
    for i in range(1, S):
        coding.append(coding[-1] + slots[i][0]) # asc
        eating.append(eating[-1] - slots[i-1][1]) # des
    eating.append(0)
    for d in range(D):
        A, B = read_ints()
        i = bi_search(coding, 0, len(coding)-1, A)
        if i != -1 and ((coding[i] - A) * (1.0*slots[i][1]/slots[i][0]) + eating[i+1] >= B):
            res.append('Y')
        else:
            res.append('N')
    print(''.join(res))


########################

T = read_int()
for i in range(T):
    print('Case #%d: '%(i+1), end='')
    solver()
