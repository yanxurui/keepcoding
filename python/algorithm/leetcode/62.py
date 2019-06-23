class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        table = [[1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]
        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (3,2),
            3
        ),
        (
            (7,3),
            28
        ),
        (
            (23,12),
            193536720
        )
    ]
    test(Solution().uniquePaths, test_data)
