from typing import List
from collections import deque
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = self.bs(arr, x)
        l = i-1
        r = i
        rst = deque()
        while k > 0:
            left = arr[l] if l >= 0 else None
            right = arr[r] if r < len(arr) else None
            if left is None:
                rst.append(right)
                r += 1
            elif right is None:
                rst.appendleft(left)
                l -= 1
            else:
                if x - left <= right - x:
                    rst.appendleft(left)
                    l -= 1
                else:
                    rst.append(right)
                    r += 1
            k -= 1
        return list(rst)

    def bs(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,2,3,4,5],
                4, 3
            ),
            [1,2,3,4]
        ),
        (
            (
                [1,2,3,4,5],
                4, -1
            ),
            [1,2,3,4]
        ),
    ]
    test(Solution().findClosestElements, test_data)

