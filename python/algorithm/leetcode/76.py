# todo: too slow
from collections import Counter
INT_MAX = 1<<31-1

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = Counter(t)
        count = len(t)
        l = r = 0
        head = None
        d = INT_MAX
        while r < len(s):
            c = counter.get(s[r], None)
            if c is not None:
                if c > 0:
                    count -= 1
                counter[s[r]] -= 1   
            r += 1
            while count == 0:
                # valid
                if r-l < d:
                    d = r-l
                    head = l
                # contract and make it invalid
                c = counter.get(s[l], None)
                if c is not None:
                    if c >= 0:
                        count += 1
                    counter[s[l]] += 1
                l += 1
        return '' if d == INT_MAX else s[head:head+d]




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
        ),
        (
            (
                "ab",
                "b"
            ),
            "b"
        ),
        (
            (
                "bba",
                "ab"
            ),
            "ba"
        )
    ]
    test(Solution().minWindow, test_data)
