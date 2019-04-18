# Amazon SDE online assessment
# state: 惨败

def countKDistinctSubstrings(inputString, num):
    # how many substrings have num distince characters
    # passed 5/12
    count = 0
    for start in range(len(inputString)-num+1):
        s = set()
        for end in range(start, len(inputString)):
            s.add(inputString[end])
            if len(s) == num:
                count += 1
            elif len(s) > num:
                break
    return count

def maxOfMinElevations(columnCount, rowCount, mat):
    # maximum of minimum elevation in the route from left-top to right-bottom
    # failed to solve in time
    for r in range(0, rowCount):
        for c in range(0, columnCount):
            if r == 0 and c == 0:
                continue
            m = -1
            if r > 0:
                up = mat[max(r-1,0)][c]
                m = max(m, up)
            if c > 0:
                left = mat[r][max(c-1,0)]
                m = max(m, left)
            if mat[r][c] > m:
                mat[r][c] = m
    return mat[rowCount-1][columnCount-1]


if __name__ == '__main__':
    from testfunc import test
    test_data1 = [
        (('pqpqs', 2), 7),
        (('abafg', 2), 5),
        (('abc', 4), 0),
        (('abc', 3), 1),
        (('abc', 2), 2),
        (('abcabc', 3), 10),
        (('', 3), 0),
        (('ababab', 3), 0),
    ]
    test(countKDistinctSubstrings, test_data1)

    test_data2 = [
        ((2, 2, [[5, 1],
                 [4, 5]]), 4),
        ((3, 3, [[6, 1, 6],
                 [4, 5, 7],
                 [2, 3, 8]]), 4),
        ((3, 3, [[5, 1, 6],
                 [4, 5, 8],
                 [2, 3, 9]]), 4),
        ((3, 3, [[5, 4, 3],
                 [4, 3, 2],
                 [3, 2, 1]]), 1),
    ]
    test(maxOfMinElevations, test_data2)
