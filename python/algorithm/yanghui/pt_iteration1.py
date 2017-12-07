def solve(n, k):
    L = [[]]
    for i in range(1, n+1):
        l = [None]
        for j in range(1, i+1):
            if j==1 or j==i:
                v = 1
            else:
                v = L[i-1][j-1] + L[i-1][j]
            if i==n and j==k:
                return v
            l.append(v)
        L.append(l)
