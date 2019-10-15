# https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # descending order
        rst = []
        for i in range(len(nums)):
            # remove idx out of (i-k, i]
            while q and q[0] <= i-k:
                q.popleft()
            # remove nums that are smaller than nums[i] from the tail
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i) # index
            if i >= k-1:
                rst.append(nums[q[0]])
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,3,-1,-3,5,3,6,7],
                3
            ),
            [3,3,5,5,6,7] 
        )
    ]
    test(Solution().maxSlidingWindow, test_data)
