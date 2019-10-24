# -*- coding:utf-8 -*-

class Parenthesis:
    def chkParenthesis(self, A, n):
        # write code here
        cnt = 0
        for c in A:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            else:
                return False
        return cnt == 0


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                '(()())',
                6
            ),
            True
        ),
        (
            (
                '()a()()',
                7
            ),
            False
        ),
        (
            (
                '()(()()',
                7
            ),
            False
        )
    ]
    test(Parenthesis().chkParenthesis, test_data)
