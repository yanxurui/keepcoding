# https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # proof
        # s: distance of slow
        # c: length of circle
        # x: distance from 0 to entry of circle
        # a: distance from entry to meet point
        # 2s = s + nc => s = nc
        # s = x + a + mc
        # x = (n-m-1)*c + c - a
        # that is, new finally will meet slow at the entry point
        new = 0
        while new != slow:
            new = nums[new]
            slow = nums[slow]
        return slow


def swap(nums, i, j):
    if nums[i] == nums[j]:
        return False
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp
    return True

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            while i != n:
                if swap(nums, i, n):
                    n = nums[i]
                else:
                    return n
        return nums[0]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,3,4,2,2],
            2
        ),
        (
            [3,1,3,4,2],
            3
        ),
        (
            [1,1,1,3],
            1
        ),
        (
            [1,1,2,3],
            1
        )
    ]
    test(Solution2().findDuplicate, test_data)

