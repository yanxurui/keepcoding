# -*- coding:utf-8 -*-
class Robot:
    def countWays(self, x, y):
        # write code here
        dp = [[0 for j in range(y)] for i in range(x)]
        for i in range(x):
            dp[i][0] = 1
        for j in range(y):
            dp[0][j] = 1
        for i in range(1, x):
            for j in range(1, y):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[x-1][y-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (2,2),
            2
        )
    ]
    test(Robot().countWays, test_data)
