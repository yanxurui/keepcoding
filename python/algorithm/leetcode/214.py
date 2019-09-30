class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        # abac => a#b#a#c
        # bbc => b#b#c
        buf = '#'.join(s)
        for m in range((len(buf)-1)//2, -1, -1):
            if self.isPalindrome(buf, m):
                break
        buf = buf[2*m+1:][::-1] + buf
        return ''.join([c for i,c in enumerate(buf) if i%2==0])

    def isPalindrome(self, buf, m):
        for i in range(1, m+1):
            if buf[m-i] != buf[m+i]:
                return False
        return True



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
