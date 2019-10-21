class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        lo = 0
        maxLen = 1
        i = 0
        d = {}
        d[s[0]] = 0
        for j in range(1, n):
            if s[j] not in d:
                d[s[j]] = j
                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    lo = i
            else:
                i = d[s[j]] + 1
                d = {}
                for k in range(i, j+1):
                    d[s[k]] = k
        return maxLen


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'abcabcbb',
            3
        ),
        (
            'bbbbb',
            1
        ),
        (
            'pwwkew',
            3
        ),
        (
            'abcad',
            4
        ),
    ]
    test(Solution().lengthOfLongestSubstring, test_data)

