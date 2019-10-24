# https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rst = []
        self.backtrack('', n, 0, 0, rst)
        return rst

    def backtrack(self, s, n, o, c, rst):
        if len(s) == 2*n:
            rst.append(s)
        else:
            if o < n:
                self.backtrack(s+'(', n, o+1, c, rst)
            if o > c:
                self.backtrack(s+')', n, o, c+1, rst)



if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            3,
            [
              "((()))",
              "(()())",
              "(())()",
              "()(())",
              "()()()"
            ]
        ),
        (
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()"
            ]
        )
    ]
    test(Solution().generateParenthesis, test_data, compare=unordered_equal)

