from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if not (i < len(s) and c == strs[j][i]):
                    break
        return strs[0][:i]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ["flower","flow","flight"],
            'fl'
        ),
        (
            ["dog","racecar","car"],
            ''
        ),
        (
            [],
            ''
        ),
    ]
    test(Solution().longestCommonPrefix, test_data)

