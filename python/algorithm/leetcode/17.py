from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        rst = ['']
        for d in digits:
            rst = [s+c for s in rst for c in letters[int(d)]]
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            '23',
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        )
    ]
    test(Solution().letterCombinations, test_data)

