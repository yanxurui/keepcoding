import operator

def c(n,k):
    if k == 0:
        return 1
    if n == k:
        return 1
    return reduce(operator.mul, range(n-k+1, n+1))/reduce(operator.mul, range(1, k+1))

def check(n, k):
    for a in (n, k):
        if type(a) is not int:
            return False
        if not (a >= 1 and a <= 30000):
            return False
    if k > n:
        return False
    return True

def solve(n, k):
    if not check(n, k):
        return None
    return c(n-1, k-1)
