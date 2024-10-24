# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/solutions/392933/java-c-python-two-pointers-and-stack-solution/
from typing import List
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]]
        for c in s:
            if c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join([c * n for c, n in stack])

if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (
                'abcd',
                2
            ),
            'abcd'
        ),
        (
            (
                'deeedbbcccbdaa',
                3
            ),
            'aa'
        ),
        (
            (
                'pbbcggttciiippooaais',
                2
            ),
            'ps'
        )
    ]
    test(Solution().removeDuplicates, test_data)
