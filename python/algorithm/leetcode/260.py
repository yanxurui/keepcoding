from typing import List
from functools import reduce
import operator

# https://leetcode.com/problems/single-number-iii/solutions/750622/python-4-lines-o-n-time-o-1-space-explained/
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = reduce(operator.xor, nums)
        d = s & (s-1) ^ s # get the last bit with 1 set
        n1 = reduce(operator.xor, filter(lambda n: n & d, nums))
        return [n1, s ^ n1]

# https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        xor = 0
        for n in nums:
            xor = xor ^ n
        mask = 1
        while not (mask & xor):
            mask = mask << 1
        a = b = 0
        for n in nums:
            if mask & n:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            [1,2,1,3,2,5],
            [3,5]
        ),
        (
            [-1,0],
            [-1,0]
        ),
        (
            [0,1],
            [0,1]
        )
    ]

    test(Solution().singleNumber, test_data, compare=unordered_equal)
