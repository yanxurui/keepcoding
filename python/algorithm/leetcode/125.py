class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = 0
        e = len(s)-1
        s = s.lower()
        while b < e:
            if not s[b].isalnum():
                b += 1
                continue
            if not s[e].isalnum():
                e -= 1
                continue
            if s[b] != s[e]:
                return False
            b += 1
            e -= 1
        return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            "A man, a plan, a canal: Panama",
            True
        ),
        (
            "race a car",
            False
        ),
        (
            "0P",
            False
        ),
    ]
    test(Solution().isPalindrome, test_data)
