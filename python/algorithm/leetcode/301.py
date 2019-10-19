# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75028/Short-Python-BFS

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            '()())()',
            ["()()()", "(())()"]
        ),
        (
            '(a)())()',
            ["(a)()()", "(a())()"]
        ),
        (
            ')(',
            [""]
        )
    ]
    test(Solution().removeInvalidParentheses, test_data, compare=unordered_equal)
