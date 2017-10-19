def answer(M, F):
    c = '0'
    while True:
        if M == '1' or F == '1':
            return sub(add(c,mul(M,F)),'1')
        if M == '0' or F == '0':
            return 'impossible'
        
        if greater(F,M):
            q, F = div(F,M)
        else:
            q, M = div(M,F)
        c = add(c,q)
        
def greater(x,y):
    return len(x)>len(y) or (len(x)==len(y) and x>y)

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

def sub(x,y):
    if x==y:
        return '0'
    assert greater(x,y), "%s>%s" % (x,y)
    L = []
    for i in range(len(x)+1):
        L.append(0)
    x = map(int, x[::-1])
    y = map(int, y[::-1])
    n = 0
    while n < len(y):
        if x[n] + L[n] >= y[n]:
            L[n] = x[n] + L[n] - y[n]
        else:
            L[n+1] = -1
            L[n] = 10 + x[n] + L[n]- y[n]
        n = n + 1
    while n < len(x):
        if x[n] + L[n] >= 0:
            L[n] = x[n] + L[n]
        else:
            L[n+1] = -1
            L[n] = 10 + x[n] + L[n]
        n = n + 1

    return ''.join(map(str, L[::-1])).lstrip('0')

def smul(x, d):
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

def mul(x, y):
    if x == '0' or y == '0':
        return '0'
    L = []
    y = y[::-1]
    for i in range(len(y)):
        L.append(smul(x, y[i]) + '0'*i)
    return reduce(add, L)

def div(x, y):
    assert greater(x,y), "%s>%s" % (x,y)
    if y=='0':
        raise ZeroDivisionError
    if y=='1':
        return x, '0'
    quotient = []
    temp = ''
    for i in x:
        temp += i
        m = 1
        s = y
        while not greater(s, temp):
            s = add(s, y)
            m = m + 1
            assert m<=10
        quotient.append(m-1)
        temp = sub(temp, sub(s, y))
        temp = temp.lstrip('0')
    remainder = temp if temp != '' else '0'
    quotient = ''.join(map(str, quotient)).lstrip('0')
    return quotient, remainder


for M,F in [
        ('1','1'),
        ('1','2'),
        ('200000','1'),
        ('4','7'),
        ('2','4'),
        ('20000000000054657567658567456','412435666545568765643657465567687958465543565767')
    ]:
    print(answer(M,F))

# for x,y in [
#         ('2','1'),
#         ('10','1'),
#         ('100','66'),
#         ('10000000000000','1'),
#         ('412435666545568765643657465567687958465543565767','20000000000054657567658567456')
#     ]:
#     print(sub(x,y))


# for x,y in [
#         ('2','1'),
#         ('5','2'),
#         ('100','25'),
#         ('10000000000000','1'),
#         ('412435666545568765643657465567687958465543565767','20000000000054657567658567456')
#     ]:
#     print(div(x,y))


