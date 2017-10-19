import pdb

# time exceeds
# output right answer
def answer0(l):
    count = 0
    length = len(l)
    if length < 3:
        return 0
    # l = sorted(l)
    for i in range(length-2):
        for j in range(i+1, length-1):
            if l[j] % l[i] == 0:
                for k in range(j+1, length):
                    if l[k] % l[j] == 0:
                        count = count + 1
    return count

# pass
def answer(l):
    count = 0
    length = len(l)
    if length < 3:
        return 0
    # m = [[]] * length
    m=[]
    for i in range(length):
        m.append([])
    for i in range(length):
        for j in range(i+1, length):
            if l[j] % l[i] == 0:
                m[j].append(i)
    for divs in reversed(m):
        count = count + sum([len(m[div]) for div in divs])
    return count

# pass
# the same as answer but more readable
def answer1(l):
    count = 0
    length = len(l)
    if length < 3:
        return 0
    # m = [[]] * length
    m=[]
    for i in range(length):
        m.append([])
    for i in range(length):
        for j in range(i+1, length):
            if l[j] % l[i] == 0:
                m[i].append(j)
    for divs in m:
        count = count + sum([len(m[div]) for div in divs])
    return count




# time exceeds
def answer2(l):
    count = 0
    length = len(l)
    if length < 3:
        return 0
    d = []
    i = 0
    while i < length:
        c = 1
        while i+c < length and l[i+c] == l[i]:
            c = c + 1
        d.append((l[i], c))
        i = i + c
    # pdb.set_trace()
    length = len(d)
    for i in range(length):
        iv,ic = d[i]
        if ic>=3:
            count = count + ic*(ic-1)*(ic-2)/6
        for j in range(i+1,length):
            jv,jc=d[j]
            if jv%iv:
                continue
            s=ic+jc
            if s>=3:
                count = count + s*(s-1)*(s-2)/6
                if ic>=3:
                    count = count - ic*(ic-1)*(ic-2)/6
                if jc>=3:
                    count = count - jc*(jc-1)*(jc-2)/6
            for k in range(j+1, length):
                kv,kc = d[k]
                if kv%jv:
                    continue
                count=count+ic*jc*kc
    return count


# time exceeds
# improve answer2
def answer22(l):
    count = 0
    length = len(l)
    if length < 3:
        return 0
    d = []
    i = 0
    while i < length:
        c = 1
        while i+c < length and l[i+c] == l[i]:
            c = c + 1
        d.append((l[i], c))
        i = i + c

    m = {}
    length = len(d)
    for i in range(length):
        m[i] = []
        iv, ic = d[i]
        for j in range(i+1,length):
            jv,jc=d[j]
            if jv%iv==0:
                m[i].append(j)

    for i in range(length):
        iv,ic = d[i]
        if ic>=3:
            count = count + ic*(ic-1)*(ic-2)/6
        for j in m[i]:
            jv,jc=d[j]
            s=ic+jc
            if s>=3:
                count = count + s*(s-1)*(s-2)/6
                if ic>=3:
                    count = count - ic*(ic-1)*(ic-2)/6
                if jc>=3:
                    count = count - jc*(jc-1)*(jc-2)/6
            for k in m[j]:
                kv,kc = d[k]
                count=count+ic*jc*kc
    return count

if __name__ == '__main__':
    from test_func import test

    input1=([1]*1999)
    input1.append(999999)
    test(answer,
        [
          ([],0),
          ([1],0),
          ([1,2],0),
          ([1,2,3],0),

          ([1,2,4],1),
          ([1,1,1],1),

          ([2,1,4],0),

          ([2,2,2,3],1),
          ([1,1,1,2],4),

          ([1,1,2,3],2),
          ([3,2,2,4],1),
          ([1,2,2,2],4),
          ([2,2,4,4,1,1],4),

          ([1,1,1,1,1,1,1,1,1,1],120),
          ([1,2,4,8,16],10),

          ([1,2,3,4,5,6],3),

          ([1 for i in range(1000)],166167000),
          ([1 for i in range(2000)],1331334000),
          ([i+1 for i in range(1000)],16287),
          ([i+1 for i in range(2000)],40888),
          ([i+1000000 for i in range(1000)],0),
          ([1,2]*1000,665667000),# time limit exceeded
          (input1, 1331334000)
        ]
        )