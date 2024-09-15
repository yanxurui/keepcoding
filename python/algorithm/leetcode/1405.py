from typing import List
class Solution:
    def recursive(self, a, b, c, aa, bb, cc):
        if b > a:
            return self.recursive(b, a, c, bb, aa, cc)
        if c > b:
            return self.recursive(a, c, b, aa, cc, bb)
        use_a = 2 if a >= 2 else a
        if b == 0:
            return aa * use_a
        use_b = 1 if a - use_a >= b else 0
        return aa * use_a + bb * use_b + self.recursive(a-use_a, b-use_b, c, aa, bb, cc)

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return self.recursive(a, b, c, 'a', 'b', 'c')

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (1,1,7),
            'ccaccbcc'
        ),
        (
            (7,1,0),
            'aabaa'
        ),
        (
            (2,4,1),
            'bbabbac'
        ),

    ]
    test(Solution().longestDiverseString, test_data)
