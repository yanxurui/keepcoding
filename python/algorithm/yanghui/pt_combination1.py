import operator

def fac(n):
    if n == 0:
        return 1 # 0! = 1
    return reduce(operator.mul, range(1,n+1))

def c(n, k):
    return fac(n)/(fac(k)*fac(n-k))

def solve(n, k):
    return c(n-1, k-1)
