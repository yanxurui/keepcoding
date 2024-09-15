from typing import List

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        r = 0
        last = 0
        for c in s:
            if c == '(':
                stack.append((c, r))
                last = 0
            elif c == ')':
                c2, r2 = stack.pop()
                assert c2 == '('
                last = r - r2
                r = r2
                if last == 0:
                    r += 1
                else:
                    r += 2 * last
        return r


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            '()',
            1
        ),
        (
            '(())',
            2
        ),
        (
            '()()',
            2
        ),
        (
            '((()))',
            4
        ),
        (
            '(()(()))',
            6
        )
    ]
    test(Solution().scoreOfParentheses, test_data)

