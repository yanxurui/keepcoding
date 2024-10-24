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

# bad
# class Solution2:
#     def shortestPalindrome(self, s: str) -> str:
#         if not s:
#             return s
#         n = len(s)
#         l = n
#         for i in range(n//2, -1, -1):
#             if i > 0 and s[0:i][::-1] == s[i:2*i]: # even
#                 return s[2*i:][::-1] + s
#             if 2*i+1 <= n and s[0:i][::-1] == s[i+1:2*i+1]: # odd
#                 return s[2*i+1:][::-1] + s
        

class Solution3:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        for i in range(len(s)-1, -1, -1):
            l = 0
            r = i
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            if l >= r:
                # found a palindrome
                return s[i+1:][::-1] + s


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
    test(Solution3().shortestPalindrome, test_data)
