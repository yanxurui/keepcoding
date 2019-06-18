class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = -1, -1
        last = None
        for i in range(len(s)):
            if s[i] == ' ':
                if not (last is None or last == ' '):
                    r = i
            else:
                if last == ' ' or last is None:
                    l = i
            last = s[i]
        if r < l:
            r = len(s)
        return r - l


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            "Hello World",
            5
        ),
        (
            " ",
            0
        ),
        (
            "a",
            1
        )
    ]
    test(Solution().lengthOfLastWord, test_data)
