# https://leetcode.com/problems/shortest-palindrome/discuss/60141/C%2B%2B-8-ms-KMP-based-O(n)-time-and-O(n)-memory-solution

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = s[::-1]
        mirror = s + '#' + rs
        # run KMP on mirror
        lps = [0] * len(mirror)
        k = 0
        for i in range(1, len(mirror)):
            while k > 0 and mirror[i] != mirror[k]:
                k = lps[k-1]
            if mirror[i] == mirror[k]:
                k += 1
            lps[i] = k
        return rs[:len(rs)-lps[-1]] + s



if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ('aacecaaa'),
            'aaacecaaa'
        ),
        (
            ('abcd'),
            'dcbabcd'
        ),
        (
            ("ba"),
            'aba'
        ),
        (
            (""),
            ''
        ),
        (
            ("abbacd"),
            "dcabbacd"
        ),
        (
            ('a'*1000000),
            'a'*1000000
        )
    ]
    test(Solution().shortestPalindrome, test_data)
