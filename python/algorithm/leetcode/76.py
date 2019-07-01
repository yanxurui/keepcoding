# todo: too slow

from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''

        left_m = 0
        right_m = -1

        T = set(t)
        # position of last occurrence
        d = defaultdict(list)
        for c in t:
            d[c].append(-1)
        left = -1
        # expand
        for right in range(len(s)):
            if s[right] in T:
                p = d[s[right]].pop(0)
                d[s[right]].append(right)
                if p == left:
                    left = min([min(l) for l in d.values()])
                if left != -1:
                    if right_m == -1 or right - left < right_m - left_m:
                        left_m = left
                        right_m = right
        if right_m == -1:
            return ''
        else:
            return s[left_m:right_m+1]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                "ADOBECODEBANC",
                "ABC"
            ),
            "BANC"
        ),
        (
            (
                "a",
                "aa"
            ),
            ""
        ),
        (
            (
                "aa",
                "aa"
            ),
            "aa"
        )
    ]
    test(Solution().minWindow, test_data)
