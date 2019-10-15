# https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66328/A-recursive-Java-solution-(284-ms)
from typing import List

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        rst = []
        import pdb
        # pdb.set_trace()
        for i, c in enumerate(input):
            if c in '+-*':
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]):
                        if c == '+':
                            rst.append(a+b)
                        elif c == '-':
                            rst.append(a-b)
                        elif c == '*':
                            rst.append(a*b)
        return rst if rst else [int(input)]


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            '2-1-1',
            [0, 2]
        ),
        (
            '2*3-4*5',
            [-34, -14, -10, -10, 10]
        )
    ]
    test(Solution().diffWaysToCompute, test_data, compare=unordered_equal)
