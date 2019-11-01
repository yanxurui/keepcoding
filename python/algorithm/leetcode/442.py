from typing import List

def swap(nums, i, j):
    if nums[i] == nums[j]:
        # 1. duplicates, stop
        # 2. i == j, already in the right position
        return False
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    return True


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # put back
            j = nums[i] - 1
            while swap(nums, i, j):
                j = nums[i] - 1
        rst = []
        for i in range(len(nums)):
            if i+1 != nums[i]:
                rst.append(nums[i])
        return rst


# https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92387/Java-Simple-Solution
class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        rst = []
        for i in range(len(nums)):
            j = abs(nums[i])-1
            if nums[j] < 0:
                rst.append(abs(nums[i]))
            # flip
            nums[j] = -nums[j]
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [4,3,2,7,8,2,3,1],
            [2, 3]
        ),
        (
            [2,1],
            []
        ),
    ]
    test(Solution2().findDuplicates, test_data, compare=unordered_equal)

