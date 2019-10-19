# https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        for l in range(2, n): # length of range
            for i in range(0, n-l): # left
                j = i + l # right
                for k in range(i+1, j): # the last ballon to burst between (i,j)
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[0][n-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [3,1,5,8],
            167
        )
    ]
    test(Solution().maxCoins, test_data)
