# -*- coding:utf-8 -*-
class Robot:
    def countWays(self, m, x, y):
        # write code here
        dp = [[0 for j in range(y)] for i in range(x)]
        for i in range(x):
            if m[i][0] == 1:
                dp[i][0] = 1
            else:
                break
        for j in range(y):
            if m[0][j] == 1:
                dp[0][j] = 1
            else:
                break
        for i in range(1, x):
            for j in range(1, y):
                if m[i][j] == 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[x-1][y-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [
                    [1,1,1],
                    [1,0,1],
                    [1,1,1],
                ],
                3, 3
            ),
            2
        ),
        (
            (
                [
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,0,1,1],
                    [0,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1]
                ],
                11,4
            ),
            196
        ),
    ]
    test(Robot().countWays, test_data)
