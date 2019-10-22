from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        rst = []
        k = 0
        while True:
            c = ''
            for i, s in enumerate(strs):
                if k >= len(s):
                    c = ''
                    break
                if i == 0:
                    c = s[k]
                else:
                    if c != s[k]:
                        c = ''
                        break
            if c:
                rst.append(c)
            else:
                break
            k += 1
        return ''.join(rst)


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

