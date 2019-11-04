# https://leetcode.com/problems/equal-rational-numbers/discuss/214203/JavaC%2B%2BPython-Easy-Cheat

class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        return self.transform(S) == self.transform(T)

    def transform(self, s):
        i = s.find('(')
        if i >= 0:
            s = s[:i] + s[i+1:-1]*20
        return float(s)



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                '0.(52)',
                '0.5(25)'
            ),
            True
        ),
        (
            (
                '0.1666(6)',
                '0.166(66)'
            ),
            True
        ),
        (
            (
                '0.9(9)',
                '1'
            ),
            True
        ),
    ]
    test(Solution().isRationalEqual, test_data)

