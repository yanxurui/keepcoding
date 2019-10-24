from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = j = 0
        while True:
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if j == len(nums):
                break
            nums[i+1] = nums[j]
            i += 1
        return i+1


def wrapper(nums):
    n = Solution().removeDuplicates(nums)
    return n, nums[:n]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1,1,2],
            (2, [1,2])
        ),
        (
            [0,0,1,1,1,2,2,3,3,4],
            (5, [0,1,2,3,4])
        ),
        
    ]
    test(wrapper, test_data)
