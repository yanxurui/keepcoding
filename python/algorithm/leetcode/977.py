# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A)-1
        rst = [0] * len(A)
        while l <= r:
            if abs(A[l]) >= abs(A[r]):
                rst[r-l] = A[l]**2
                l += 1
            else:
                rst[r-l] = A[r]**2
                r -= 1
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [-4,-1,0,3,10],
            [0,1,9,16,100]
        ),
        (
            [-7,-3,2,3,11],
            [4,9,9,49,121]
        ),
    ]
    test(Solution().sortedSquares, test_data)

