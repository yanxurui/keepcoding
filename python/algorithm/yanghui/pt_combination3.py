import operator

def c(n,k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return reduce(operator.mul, range(n-k+1, n+1))/reduce(operator.mul, range(1, k+1))

def solve(n, k):
    return c(n-1, k-1)
