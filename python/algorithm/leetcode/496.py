# https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C%2B%2B-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # sum(P) - sum(N) = target
        # 2*sum(P) = target + sum(P) + sum(N)
        # sum(P) = (target + sum(nums))//2
        sum_of_arr = sum(nums)
        if S > sum_of_arr:
            return 0
        if (S+sum_of_arr) % 2 == 1:
            return 0
        return self.find(nums, (S+sum_of_arr)//2)

    def find(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for n in nums:
            for t in range(target, n-1, -1): # reverse order means n can only be used once
                dp[t] += dp[t-n]
        return dp[target]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1, 1, 1, 1, 1],
                3
            ),
            5
        )
    ]
    test(Solution().findTargetSumWays, test_data)

