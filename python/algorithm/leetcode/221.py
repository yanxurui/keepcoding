class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        tab = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                # row
                r = i
                while r >= 0 and matrix[r][j] == '1':
                    r -= 1
                r = i - r
                # column
                c = j
                while c >=0 and matrix[i][c] == '1':
                    c -= 1
                c = j - c
                tab[i+1][j+1] = min([tab[i][j]+1, r, c])
        return max([max(l) for l in tab])**2


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([
                ['1', '0', '1', '0', '0'],
                ['1', '0', '1', '1', '1'],
                ['1', '1', '1', '1', '1'],
                ['1', '0', '0', '1', '0'],
            ]),
            4
        ),
        (
            ([]),
            0
        ),
        (
            ([
                ["0","0","0","1"],
                ["1","1","0","1"],
                ["1","1","1","1"],
                ["0","1","1","1"],
                ["0","1","1","1"]
            ]),
            9
        )
        
    ]
    test(Solution().maximalSquare, test_data)
