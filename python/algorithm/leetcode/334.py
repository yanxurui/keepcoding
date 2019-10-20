from typing import List
import sys
INT_MAX = sys.maxsize

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # dp[i] represents the smallest last number in an increasing seq of length i
        l = 3
        dp = [INT_MAX] * (l+1)
        dp[0] = -dp[0]
        for n in nums:
            for i in range(l):
                if n > dp[i]:
                    if n < dp[i+1]:
                        dp[i+1] = n
                        if i+1 == l:
                            return True
                else:
                    break
        return False
        

if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            [1,2,3,4,5],
            True
        ),
        (
            [5,4,3,2,1],
            False
        ),
        (
            [1,3,0,5],
            True
        ),
        (
            [1,2,-10,-8,-7],
            True
        )
    ]
    test(Solution().increasingTriplet, test_data)
