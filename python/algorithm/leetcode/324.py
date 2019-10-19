# https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        half = n - n//2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]

def wrapper(nums):
    Solution().wiggleSort(nums)
    return nums

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1, 5, 1, 1, 6, 4],
            [1, 6, 1, 5, 1, 4]
        ),
        (
            [1, 3, 2, 2, 3, 1],
            [2, 3, 1, 3, 1, 2]
        ),
        (
            [4,5,5,6],
            [5,6,4,5]
        ),
    ]
    test(wrapper, test_data)
