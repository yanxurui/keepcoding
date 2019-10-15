# https://leetcode.com/problems/expression-add-operators/discuss/71895/Java-Standard-Backtrace-AC-Solutoin-short-and-clear
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        rst = []
        self.util(num, target, 0, rst, '', 0, None)
        return rst

    def util(self, num, target, pos, rst, exp, val, multed):
        if pos == len(num):
            if val == target:
                rst.append(exp)
        else:
            for i in range(pos, len(num)):
                op = num[pos:i+1]
                if i > pos and num[pos] == '0':
                    break
                elif pos == 0:
                    self.util(num, target, i+1, rst, op, int(op), int(op))
                else:
                    self.util(num, target, i+1, rst, exp+'+'+op, val+int(op), int(op))
                    self.util(num, target, i+1, rst, exp+'-'+op, val-int(op), -int(op))
                    self.util(num, target, i+1, rst, exp+'*'+op, val-multed+multed*int(op), multed*int(op))


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                '123',
                6
            ),
            ["1+2+3", "1*2*3"]
        ),
        (
            (
                '232',
                8
            ),
            ["2*3+2", "2+3*2"]
        ),
        (
            (
                '105',
                5
            ),
            ["1*0+5","10-5"]
        ),
        (
            (
                '00',
                0
            ),
            ["0+0", "0-0", "0*0"]
        ),
        (
            (
                '3456237490',
                9191
            ),
            []
        )
    ]
    test(Solution().addOperators, test_data, compare=unordered_equal)
