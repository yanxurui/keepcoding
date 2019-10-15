from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0

        n = len(nums)
        while True:
            while i < n and nums[i]:
                i += 1
            j = max(i, j) + 1
            while j < n and not nums[j]:
                j += 1
            # i points the first zero
            # j points the first non-zero after i
            # between [i, j) are zeros
            if i == n or j == n:
                break
            self.swap(nums, i, j)

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

def wrapper(nums):
    Solution().moveZeroes(nums)
    return nums


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [0,1,0,3,12],
            [1,3,12,0,0]
        ),
        (
            [0,0],
            [0,0]
        ),
        (
            [0,1,2,3,4],
            [1,2,3,4,0]
        ),
    ]
    test(wrapper, test_data)
