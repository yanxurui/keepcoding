import pdb

def answer(xs):
    # your code here
    def cmp_ignore_sign(x, y):
        if abs(x) < abs(y):
            return -1
        elif abs(x) > abs(y):
            return 1
        return 0

    if len(xs) == 1 and xs[0] < 0:
        return str(xs[0])
    xs = filter(lambda e: abs(e) != 0, xs)
    xs = sorted(xs, cmp_ignore_sign)
    positive = True
    first_negative = -1
    for i in range(len(xs)):
        if xs[i] < 0:
            positive = not positive
            if first_negative == -1:
                first_negative = i    
    if not positive:
        del xs[first_negative]
    xs = map(str, map(abs, xs))
    # print(xs)

    if len(xs) == 0:
        return '0'
    return reduce(multiple, xs)


def add(x, y):
    L = []
    x = x[::-1]
    y = y[::-1]

    if len(x) < len(y):
        temp = x
        x = y
        y = temp
    for i in range(len(x)):
        L.append(0)
    L.append(0)
    n = 0
    while n < len(y):
        s = int(x[n]) + int(y[n]) + L[n]
        if s >= 10:
            L[n+1] = 1
        L[n] = s % 10
        n = n + 1
    while n < len(x):
        s = int(x[n]) + L[n]
        if s >= 10:
            L[n+1] = 1
        L[n] = s % 10
        n = n + 1
    if L[n] == 0:
        L.pop()
    return ''.join(map(str, L[::-1]))

def multiple(x, y):
    def submul(x, d):
        d = int(d)
        if d == 0:
            return '0'
        if d == 1:
            return x
        L = []
        x = x[::-1]
        for i in range(len(x)):
            L.append(0)
        L.append(0)
        n = 0
        while n < len(x):
            p = int(x[n]) * d + L[n]
            if p >= 10:
                L[n+1] = p / 10
            L[n] = p % 10
            n = n + 1
        if L[n] == 0:
            L.pop()
        return ''.join(map(str, L[::-1]))
    if x == '0' or y == '0':
        return '0'
    L = []
    y = y[::-1]
    for i in range(len(y)):
        L.append(submul(x, y[i]) + '0'*i)
    return reduce(add, L)


# for x, y in [
#     ('1','2'),
#     ('10','1'),
#     ('1','10'),
#     ('100','201'),
#     ('1000000000','1'),
#     ('123','1234567890'),
#     ('1','99999')]:
#     print("%s + %s = %s" % (x,y,add(x,y)))


# for x, y in [
#     ('1','2'),
#     ('10','1'),
#     ('1','10'),
#     ('4','5'),
#     ('25','25'),
#     ('100','10000'),
#     ('250','4000'),
#     ('111','0'),
#     ('0','100')
#     ]:
#     print("%s x %s = %s" % (x,y,multiple(x,y)))



xss = [
[-1],#case 4
[0, 0, 0], #case 3
[2, 0, 2, 2, 0],
[-2, -3, 4, -5],
[19, -2, -3, -5, -10000000,599]
]
for xs in xss:
    print(answer(xs))
