from typing import List
import sys
INT_MAX = sys.maxsize

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = [INT_MAX] * (len(nums)+1)
        dp[0] = 0
        for k in range(1, m+1):
            # dp[i] means the min largest sum among k-1 subarrays in nums[0:i], i.e., the first i elements
            for i in range(len(nums), k-1, -1):
                s = 0
                for l in range(1, i-k+2):
                    s += nums[i-l]
                    if s > dp[i]:
                        break
                    dp[i] = min(dp[i], max(dp[i-l], s))
        return dp[len(nums)]

# https://leetcode.com/problems/split-array-largest-sum/discuss/89835/Java-easy-binary-search-solution-8ms
class Solution2:
    def splitArray(self, nums: List[int], m: int) -> int:
        l = max(nums)
        h = sum(nums)
        while l < h:
            mid = l + (h-l)//2
            if self.valid(nums, m, mid):
                h = mid
            else:
                l = mid + 1
        return h

    def valid(self, nums, m, maximum):
        cnt = 0
        cur = 0
        for n in nums:
            cur += n
            if cur > maximum:
                cur = n
                cnt += 1
                if cnt > m:
                    return False
        cnt += 1
        return cnt <= m


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [7,2,5,10,8],
                2
            ),
            18
        )
    ]
    test(Solution2().splitArray, test_data)

