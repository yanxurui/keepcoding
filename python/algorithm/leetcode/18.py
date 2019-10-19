# https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        rst = []
        self.NSum(nums, 4, 0, len(nums)-1, target, [], rst)
        return rst

    def NSum(self, nums, N, l, r, target, tmp, rst):
        if r - l + 1 < N or target < nums[l] * N or target > nums[r] * N:
            return # early termination
        if N == 2:
            while l < r:
                if nums[l] + nums[r] == target:
                    rst.append(tmp + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(l, r-N+2):
                if i == l or nums[i] != nums[i-1]:
                    self.NSum(nums, N-1, i+1, r, target-nums[i], tmp+[nums[i]], rst)


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            (
                [1, 0, -1, 0, -2, 2],
                0
            ),
            [
              [-1,  0, 0, 1],
              [-2, -1, 1, 2],
              [-2,  0, 0, 2]
            ]
        ),
        (
            (
                [0,0,0,0],
                0
            ),
            [[0,0,0,0]]
        )
    ]
    test(Solution().fourSum, test_data, compare=unordered_equal)

