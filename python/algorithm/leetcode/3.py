class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = 0
        d = {}
        for j in range(len(s)):
            if s[j] not in d or d[s[j]] < i:
                if j - i + 1 > maxLen:
                    maxLen = j - i + 1
            else:
                i = d[s[j]] + 1
            d[s[j]] = j
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
        (
            "tmmzuxt",
            5
        ),
    ]
    test(Solution().lengthOfLongestSubstring, test_data)

