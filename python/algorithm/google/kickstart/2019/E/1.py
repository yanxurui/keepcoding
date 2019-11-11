import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return tuple(map(int, sys.stdin.readline().split()))

########################

def find(par, x):
    if par[x] == x:
        return x
    par[x] = find(par, par[x])
    return par[x]

def solver(case):
    N, M = read_ints()
    par = [i for i in range(N)]
    S = N
    for i in range(M):
        C, D = read_ints()
        x = find(par, C-1)
        y = find(par, D-1)
        if x != y:
            # marge
            par[x] = y
            S -= 1
    print('Case #%d: %d'%(case, N-1+S-1))


########################

T = read_int()
for i in range(T):
    solver(i+1)

