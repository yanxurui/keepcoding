# https://leetcode.com/problems/coin-change/discuss/77360/C%2B%2B-O(n*amount)-time-O(amount)-space-DP-solution
import sys
from typing import List

INT_MAX = sys.maxsize

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [INT_MAX] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        return dp[amount] if dp[amount] <= amount else -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1, 2, 5],
                11
            ),
            3
        ),
        (
            (
                [2],
                3
            ),
            -1
        ),
        (
            (
                [1,2,5],
                10
            ),
            2
        ),
        (
            (
                [1,2,5],
                100
            ),
            20
        ),
        (
            (
                [368,305,204,88,148,423,296,125,346],
                7163
            ),
            18
        ),
        (
            (
                [1],
                1
            ),
            1
        )
    ]
    test(Solution().coinChange, test_data)

