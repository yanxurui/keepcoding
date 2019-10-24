# -*- coding:utf-8 -*-
class Coins:
    def countWays(self, n):
        # write code here   
        dp = [0] * (n+1)
        dp[0] = 1
        coins = [1, 5, 10, 25]
        for i in range(len(coins)):
            for j in range(coins[i], n+1):
                dp[j] += dp[j-coins[i]]
                dp[j] %= 1000000007
        return dp[n]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            6,
            2
        )
    ]
    test(Coins().countWays, test_data)
