# https://leetcode.com/problems/next-greater-element-i/solutions/97595/java-10-lines-linear-time-complexity-o-n-with-explanation/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []
        for n in nums2:
            while stack and stack[-1] < n:
                p = stack.pop()
                nextGreater[p] = n
            stack.append(n)
        ans = []
        for m in nums1:
            ans.append(nextGreater.get(m, -1))
        return ans

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [4,1,2],
                [1,3,4,2]
            ),
            [-1,3,-1]
        ),
        (
            (
                [2,4],
                [1,2,3,4],
            ),
            [3,-1]
        )
    ]
    test(Solution().nextGreaterElement, test_data)

