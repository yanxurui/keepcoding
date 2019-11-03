import sys
from typing import List
INT_MIN = -sys.maxsize

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = max2 = max3 = INT_MIN
        for n in nums:
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif max1 > n > max2:
                max3 = max2
                max2 = n
            elif max2 > n > max3:
                max3 = n
        return max1 if max3 == INT_MIN else max3


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [3, 2, 1],
            1
        ),
        (
            [1, 2],
            2
        ),
        (
            [2, 2, 3, 1],
            1
        ),
        (
            [1,2,-2147483648],
            -2147483648
        ),

    ]
    test(Solution().thirdMax, test_data)

