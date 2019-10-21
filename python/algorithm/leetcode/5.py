# https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        self.maxLen = 0
        self.lo = 0
        for i in range(len(s)):
            self.expand(s, i, i) # odd
            self.expand(s, i, i+1) # even
        return s[self.lo:self.lo+self.maxLen]

    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        l = j - i - 1
        if l > self.maxLen:
            self.maxLen = l
            self.lo = i + 1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'babad',
            'bab'
        ),
        (
            'cbbd',
            'bb'
        ),
        (
            '',
            ''
        ),
        (
            'a',
            'a'
        ),
    ]
    test(Solution().longestPalindrome, test_data)
