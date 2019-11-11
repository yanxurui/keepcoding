import sys
from collections import defaultdict

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return tuple(map(int, sys.stdin.readline().split()))


def solve():
    K, J = read_ints()
    d = defaultdict(list)
    for i in range(K):
        X, Y = sys.stdin.readline().rstrip().split(' ')
        d[Y].append(X)
    delayed = sys.stdin.readline().rstrip().split(' ')
    rst = set()
    for p in delayed:
        q = [p]
        while q:
            p = q.pop(0)
            rst.add(p)
            q.extend(d[p])
    return sorted(list(rst))


if __name__ == '__main__':
    C = read_int()
    for i in range(1, C+1):
        rst = solve()
        print('Case #%d: %s' % (i, ' '.join(rst)))
    
