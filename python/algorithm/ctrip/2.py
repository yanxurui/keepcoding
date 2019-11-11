import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return tuple(map(int, sys.stdin.readline().split()))

def add_tuple(t1, t2):
    return (a+b for a,b in zip(t1, t2))

def main():
    m, n = read_ints()
    if not m or not n:
        return
    mask = [[0 for j in range(n)] for i in range(m)]
    matrix = []
    for i in range(m):
        matrix.append(read_ints())
    assert len(matrix) == m
    assert len(matrix[0]) == n
    i = j = 0
    rst = []
    # right, down, left, up
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    cur = 0
    while True:
        mask[i][j] = 1
        rst.append(matrix[i][j])
        x, y = add_tuple((i,j), directions[cur])
        if 0 <= x < m and 0 <= y < n and mask[x][y] == 0:
            i, j = x, y
        else:
            # can not walk along the current direction
            cur = (cur+1) % len(directions)
            x, y = add_tuple((i,j), directions[cur])
            if 0 <= x < m and 0 <= y < n and mask[x][y] == 0:
                i, j = x, y
            else:
                break
    print(','.join(map(str, rst)))

if __name__ == '__main__':
    main()

