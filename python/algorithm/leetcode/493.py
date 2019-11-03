# https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22
from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        bit = [0] * (len(nums) + 1)
        rst = 0
        nums_cp = sorted(nums)
        for n in nums:
            rst += self.bit_search(bit, self.index(nums_cp, 2*n+1))
            self.bit_insert(bit, self.index(nums_cp, n))
        return rst

    def index(self, nums, target):
        # find the index of target in bit
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l + 1

    def bit_search(self, bit, i):
        rst = 0
        while i < len(bit):
            rst += bit[i]
            i += i&(-i)
        return rst

    def bit_insert(self, bit, i):
        while i > 0:
            bit[i] += 1
            i -= i&(-i)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,3,2,3,1],
            2
        ),
        (
            [2,4,3,5,1],
            3
        ),
        (
            list(range(50000, 0, -1)),
            624975000
        ),
    ]
    test(Solution().reversePairs, test_data)

