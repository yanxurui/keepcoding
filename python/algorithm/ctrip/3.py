import sys

def abs(a, b):
    if a > b:
        return abs(b, a)
    return b - a

def read_int():
    return int(sys.stdin.readline())

def bs(b, e, n):
    m = (b+e)/2
    tmp = m ** 2
    if abs(tmp, n) < 0.000001:
        return m
    elif tmp < n:
        return bs(m, e, n)
    else:
        return bs(b, m, n)


def main():
    n = read_int()
    print('{:.4f}'.format(bs(0, n, n)))


if __name__ == '__main__':
    main()

