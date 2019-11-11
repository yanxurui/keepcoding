from sys import stdin
from collections import defaultdict

def read_int():
    return int(stdin.readline())

def read_ints():
    return tuple(map(int, stdin.readline().split()))

def line():
    return stdin.readline().rstrip()

def mean(nums):
    return sum(nums)//len(nums)

def solve():
    line()
    N = read_int()
    d = defaultdict(list)
    for i in range(N):
        food, price = line().split(' ')
        d[food].append(int(price))
    rst = []
    for f, ps in d.items():
        rst.append('%s %d %d %d' % (f, min(ps), max(ps), mean(ps)))
    return sorted(rst)
        


if __name__ == '__main__':
    C = read_int()
    for i in range(1, C+1):
        rst = solve()
        print('Case #%d:' % i)
        print('\n'.join(rst))
        print('')
    
