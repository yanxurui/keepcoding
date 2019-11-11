import sys
from collections import defaultdict

def flip_line(matrix, locations):
    x, y = locations[0]
    start = matrix[x][y]
    tmp = 0
    for i, j in locations[1:]:
        if matrix[i][j] == ' ':
            return 0
        elif matrix[i][j] == start:
            break
        else:
            tmp += 1
    if tmp:
        for i, j in locations[1:]:
            if matrix[i][j] != start:
                matrix[i][j] = start
            else:
                break
    return tmp


def flip(matrix, r, c):
    n = 0
    # up
    n += flip_line(matrix, zip(range(r, -1, -1), (c,)*8))
    # down
    n += flip_line(matrix, zip(range(r, 8), (c,)*8))
    # left
    n += flip_line(matrix, zip((r,)*8, range(c, -1, -1)))
    # right
    n += flip_line(matrix, zip((r,)*8, range(c, 8)))
    # 315
    n += flip_line(matrix, zip(range(r, -1, -1), range(c, -1, -1)))
    # 45
    n += flip_line(matrix, zip(range(r, -1, -1), range(c, 8)))
    # 135
    n += flip_line(matrix, zip(range(r, 8), range(c, 8)))
    # 225
    n += flip_line(matrix, zip(range(r, 8), range(c, -1, -1)))
    return n


def check(matrix, r, c, black):
    if matrix[r][c] != ' ':
        return False
        # print('ERROR %d:%s' % (i+1, step))
        # exit(0)
    else:
        matrix[r][c] = 'x' if black else 'o'
        return flip(matrix, r, c)

def main():
    # initialize
    matrix = [[' ' for j in range(8)] for i in range(8)]
    matrix[3][4] = matrix[4][3] = 'x'
    matrix[3][3] = matrix[4][4] = 'o'

    # move step by step
    black = True
    for s,step in enumerate(sys.stdin.readline().rstrip().split(',')):
        if step == '00':
            # check every blank
            for i in range(8):
                for j in range(8):
                    if matrix[i][j] == ' ' and check(matrix, i, j, black):
                        print('ERROR %d:%s' % (s+1, step))
                        exit(0)
                    matrix[i][j] = ' '
        else:
            r = int(step[1])-1
            c = 'ABCDEFGH'.index(step[0])
            if not check(matrix, r, c, black):
                print('ERROR %d:%s' % (s+1, step))
                exit(0)
        black = not black

    # count
    cnt = defaultdict(int)
    for i in range(8):
        for j in range(8):
            if matrix[i][j] != ' ':
                cnt[matrix[i][j]] += 1

    print('OK %d:%d' % (cnt['x'], cnt['o']))

if __name__ == '__main__':
    main()
