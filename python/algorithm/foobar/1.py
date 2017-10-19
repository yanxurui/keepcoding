import sys


def answer(n):
    def gen_primes():
        """ Generate an infinite sequence of prime numbers.
        """
        D = {}
        q = 2
        
        while True:
            if q not in D:
                # q is a new prime.
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            
            q += 1
    
    i, j = 0, 0
    L = []
    for p in gen_primes():
        s = str(p)
        j = j + len(s)

        if j > n:
            L.append(s)
        else:
            i = i + len(s)
        if j >= n + 5:
            break
    temp = ''.join(L)
    return temp[n-i:n+5-i]


print(answer(int(sys.argv[1])))
