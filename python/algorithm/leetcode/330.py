# https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation

from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        add = 0
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                add += 1
        return add


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                [1,3],
                6
            ),
            1
        ),
        (
            (
                [1,5,10],
                20
            ),
            2
        ),
        (
            (
                [1,2,2],
                5
            ),
            0
        ),
        (
            (
                [1,2,31,33],
                2147483647
            ),
            28
        )
    ]
    test(Solution().minPatches, test_data)
