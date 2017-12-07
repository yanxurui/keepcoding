def solve(n, k):
    for i in range(1, n+1):
        l = [None]
        for j in range(1, i+1):
            if j==1 or j==i:
                v = 1
            else:
                v = ll[j-1] + ll[j]
            l.append(v)
        ll = l # keep last line
    return ll[k]
