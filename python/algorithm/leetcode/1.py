# https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, a in enumerate(nums):
            b = target - a
            if b in d:
                return [d[b], i]
            else:
                d[a] = i


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [2, 7, 11, 15],
                9
            ),
            [0, 1]
        )
    ]
    test(Solution().twoSum, test_data)

