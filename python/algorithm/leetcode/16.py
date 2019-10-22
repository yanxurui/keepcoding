 #https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution
import sys
from typing import List

INT_MAX = sys.maxsize

def abs(a):
    return a if a >= 0 else -a

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        rst = None
        min_d = INT_MAX
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                s = target - nums[i]
                l = i + 1
                h = len(nums) - 1
                while l < h:
                    d = nums[l] + nums[h] - s
                    if abs(d) < min_d:
                        min_d = abs(d)
                        rst = nums[i] + nums[l] + nums[h]
                    if d == 0:
                        return target
                    elif d < 0:
                        l += 1
                    else:
                        h -= 1
        return rst
                            


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                [-1, 2, 1, -4],
                1
            ),
            2
        )
    ]
    test(Solution().threeSumClosest, test_data)

