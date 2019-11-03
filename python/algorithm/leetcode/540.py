# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100754/Java-Binary-Search-short-(7l)-O(log(n))-w-explanations
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b, e = 0, len(nums)-1
        while b < e:
            m = b + (e-b)//2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m+1]:
                b = m + 2
            else:
                e = m
        assert b == e
        return nums[b]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,1,2,3,3,4,4,8,8],
            2
        ),
        (
            [3,3,7,7,10,11,11],
            10
        ),
        (
            [3,3,4],
            4
        ),
    ]
    test(Solution().singleNonDuplicate, test_data)

