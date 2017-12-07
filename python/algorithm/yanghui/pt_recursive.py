def solve(n, k):
    if k==1 or k==n:
        return 1
    return solve(n-1, k-1) + solve(n-1, k)
