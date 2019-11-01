from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.KSum(nums, 2)

    def KSum(self, nums, k):
        s = sum(nums)
        nums.sort(reverse=True)
        mask = [0] * len(nums)
        return s % k == 0 and self.sub(nums, mask, 0, 0, k, s//k)

    def sub(self, nums, mask, cum_sum, start, k, target):
        if k == 1:
            return True
        if cum_sum == target:
            return self.sub(nums, mask, 0, 0, k-1, target)
        elif cum_sum > target:
            # pruning
            return False
        elif cum_sum + sum(nums[start:]) < target:
            return False
        for i in range(start, len(nums)):
            if mask[i] == 0:
                mask[i] = 1
                if self.sub(nums, mask, cum_sum + nums[i], i+1, k, target):
                    return True
                mask[i] = 0
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1, 5, 11, 5],
            True
        ),
        (
            [1, 2, 3, 5],
            False
        ),
        (
            [23,13,11,7,6,5,5],
            True
        ),
        (
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100],
            False
        ),
    ]
    test(Solution().canPartition, test_data)

