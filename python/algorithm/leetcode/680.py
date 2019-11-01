class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j and s[i] == s[j]:
            i += 1
            j -=1
        if not (i < j):
            return True
        # find the first mismatch char, skip the left one or the right one
        return self.isPalindrome(s, i, j-1) or self.isPalindrome(s, i+1, j)
    def isPalindrome(self, s, i, j):
        while i < j and s[i] == s[j]:
            i += 1
            j -=1
        return s[i] == s[j]
        


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'aba',
            True
        ),
        (
            'abca',
            True
        )
    ]
    test(Solution().validPalindrome, test_data)

