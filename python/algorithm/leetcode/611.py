# https://leetcode.com/problems/valid-triangle-number/discuss/104174/Java-O(n2)-Time-O(1)-Space
from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [2,2,3,4],
            3
        ),
        (
            [0,1,1,1],
            1
        ),
    ]
    test(Solution().triangleNumber, test_data)

