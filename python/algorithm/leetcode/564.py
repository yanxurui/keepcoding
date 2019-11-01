# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation
import sys
INT_MAX = sys.maxsize

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        candidates = []
        if len(n) > 1:
            candidates.append('9' * (len(n)-1))
        pref = n[:(len(n)+1)//2]
        pref_int = int(pref)
        for p in map(str, (pref_int-1, pref_int, pref_int+1)):
            candidates.append(p+p[:(len(n)-len(pref))][::-1])
        # print(candidates)
        diff = INT_MAX
        rst = None
        target = int(n)
        for can in candidates:
            if can == n:
                continue
            d = abs(int(can)-target)
            if d < diff:
                diff = d
                rst = can
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            '123',
            '121'
        ),
        (
            '100',
            '99'
        ),
        (
            '1',
            '0'
        ),
        (
            '10',
            '9'
        ),
    ]
    test(Solution().nearestPalindromic, test_data)

