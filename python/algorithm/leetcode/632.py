# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution

INT_MAX = 1<<31-1
INT_MIN = -(1<<31)
import heapq
from typing import List
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # (current value, row number, index of current value in the row)
        heap = [(nums[i][0],i,0) for i in range(len(nums))]
        heapq.heapify(heap)
        rst = [INT_MIN, INT_MAX]
        right = max([row[0] for row in nums])
        while True:
            left, i, j = heapq.heappop(heap)
            if right - left < rst[1] - rst[0]:
                rst = [left, right]
            if j == len(nums[i]) - 1:
                return rst
            next_value = nums[i][j+1]
            right = max(right, next_value)
            heapq.heappush(heap, (next_value, i, j+1))


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
            ),
            [20, 24]
        )
    ]
    test(Solution().smallestRange, test_data)

