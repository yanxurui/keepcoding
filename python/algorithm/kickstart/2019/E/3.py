import sys
from math import ceil


def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return tuple(map(int, sys.stdin.readline().split()))

########################

def primes(N):
    # Sieve of Eratosthenes
    res = []
    isPrime = [True for i in range(N)]
    for i in range(2, N):
        if isPrime[i]:
            res.append(i)
            for j in range(i*i, N, i):
                isPrime[j] = False
    return res
    # res = set([])
    # for i in range(max(2, l), r+1):
    #     prime = True
    #     for j in range(2, int(i**0.5)+1):
    #         if i % j == 0:
    #             prime = False
    #             break
    #     if prime:
    #         res.add(i)
    # return res
def primes_range(L, R, tab):
    # Sieve in range [L, R]
    res = []
    isPrime = [True for i in range(R-L+1)]
    for i in tab:
        l = max(i, int(ceil(1.0*L/i)))*i
        r = (R/i+1)*i
        for j in range(l, r, i):
            isPrime[j-L] = False
    return [i+L for i,yes in enumerate(isPrime) if yes]


def solver(tab):
    L, R = read_ints()
    count = 0
    # X = d1d2...dk * 2^x
    # |k(x-1)| <= 2
    # case 1: x=0, k=1,2
    S = primes_range(L, R, tab)
    # case 2: x=1, k=any, X = 2*(2y+1) = 4y+2
    for i in range(L, R+1):
        if i % 2 == 0 and (i-2)%4 == 0:
            S.append(i)
    # case 3: x=2, k=1,2
    S.extend([4*i for i in primes_range(int(ceil(L/4.0)), R/4, tab)])
    # case 4: x=3, k=1
    if L <= 8 and R >= 8:
        S.append(8)
    return len(set(S))


########################

T = read_int()
for i in range(T):
    # pre-compute
    tab = primes(int(10**(9/2.0))+1)
    print('Case #%d: %s'%((i+1), str(solver(tab))))


