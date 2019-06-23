class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        # the first row
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                for k in range(j, n):
                    obstacleGrid[0][k] = 0
                break
            else:
                obstacleGrid[0][j] = 1
        # the first column
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                for k in range(i, m):
                    obstacleGrid[k][0] = 0
                break
            else:
                obstacleGrid[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    # not obstacle
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ],
            2
        ),
        (
            [
                [0,1,0],
                [0,1,0],
                [0,0,0]
            ],
            1
        ),
        (
            [[1],[0]],
            0
        )
    ]
    test(Solution().uniquePathsWithObstacles, test_data)
