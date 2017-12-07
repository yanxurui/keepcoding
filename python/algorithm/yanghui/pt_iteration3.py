# add 0 in 2 sides
def triangles1():
    l = [1]
    while True:
        yield l
        l.append(0)
        l = [l[i-1] + l[i] for i in range(len(l))]

# zip
def triangles2():
    l = [1]
    while True:
        yield l
        l = [sum(t) for t in zip([0]+l, l+[0])]

def solve(n, k):
    for l in triangles1():
        n -= 1
        if n==0:
            return l[k-1]
