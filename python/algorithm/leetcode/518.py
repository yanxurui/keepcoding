import sys
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
        return dp[amount]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                5,
                [1, 2, 5]
            ),
            4
        ),
        (
            (
                3,
                [2]
            ),
            0
        ),
        (
            (
                10,
                [10] 
            ),
            1
        ),
    ]
    test(Solution().change, test_data)

