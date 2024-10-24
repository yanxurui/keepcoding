from typing import List

# https://leetcode.com/problems/132-pattern/solutions/4107421/99-35-stack-left-approach-binary-search/
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')
        for n in reversed(nums):
            if n < third:
                return True
            while stack and n > stack[-1]:
                third = stack.pop()
            stack.append(n)
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,2,3,4],
            False
        ),
        (
            [3,1,4,2],
            True
        ),
        (
            [-1,3,2,0],
            True
        ),
        (
            [1,0,1,-4,-3],
            False
        )
    ]
    test(Solution().find132pattern, test_data)

