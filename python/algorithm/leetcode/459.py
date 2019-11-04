# https://leetcode.com/problems/repeated-substring-pattern/discuss/94334/Easy-python-solution-with-explaination

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s)[1:-1].find(s) != -1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'abab',
            True
        ),
        (
            'aba',
            False
        ),
        (
            'abcabcabcabc',
            True
        ),
    ]
    test(Solution().repeatedSubstringPattern, test_data)

