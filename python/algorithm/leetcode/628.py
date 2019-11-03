# https://leetcode.com/problems/maximum-product-of-three-numbers/discuss/104729/Java-O(1)-space-O(n)-time-solution-beat-100
from typing import List

INT_MAX = 1<<31-1
INT_MIN = -(1<<31)

class Solution:
    def maximumProduct(self, nums: List[int]) -> int: 
        max1 = max2 = max3 = INT_MIN
        min1 = min2 = INT_MAX
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n

            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n 
        return max(max1*max2*max3, max1*min1*min2)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,2,3],
            6
        ),
        (
            [1,2,3,4],
            24
        ),
        (
            [-1,-2,-3],
            -6
        ),
        
    ]
    test(Solution().maximumProduct, test_data)

