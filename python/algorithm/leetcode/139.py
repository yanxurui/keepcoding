# https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        f = [False] * (n+1)
        f[0] = True

        for i in range(1, n+1):
            for j in range(i):
                f[i] = f[j] and (s[j:i] in wordDict)
                if f[i]:
                    break
        return f[n]


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                "leetcode",
                ["leet", "code"]
            ),
            True
        ),
        (
            (
                "applepenapple",
                ["apple", "pen"]
            ),
            True
        ),
        (
            (
                "catsandog",
                ["cats", "dog", "sand", "and", "cat"]
            ),
            False
        )
    ]
    test(Solution().wordBreak, test_data)
