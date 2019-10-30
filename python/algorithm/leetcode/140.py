# https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS/43441

class Solution(object):
    def __init__(self):
        self.d = {}

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return []
        if s in self.d:
            return self.d[s]
        res = []
        for i in range(n):
            if s[i:] in wordDict:
                if i > 0:
                    tmp = self.wordBreak(s[:i], wordDict)
                    for t in tmp:
                        res.append(t + ' ' + s[i:])
                else:
                    res.append(s[i:])
        self.d[s] = res
        return res

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return []
        if s in self.d:
            return self.d[s]
        res = []
        for i in range(1, n+1):
            if s[:i] in wordDict:
                if i < n:
                    tmp = self.wordBreak(s[i:], wordDict)
                    for t in tmp:
                        res.append(s[:i] + ' ' + t)
                else:
                    res.append(s[:i])
        self.d[s] = res
        return res


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            (
                "catsanddog",
                ["cat", "cats", "and", "sand", "dog"]
            ),
            [
                "cats and dog",
                "cat sand dog"
            ]
        ),
        (
            (
                "pineapplepenapple",
                ["apple", "pen", "applepen", "pine", "pineapple"]
            ),
            [
                "pine apple pen apple",
                "pineapple pen apple",
                "pine applepen apple"
            ]
        ),
        (
            (
                "catsandog",
                ["cats", "dog", "sand", "and", "cat"]
            ),
            []
        ),
        (
            (
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
            ),
            []
        )
    ]
    test(Solution().wordBreak2, test_data, compare=unordered_equal)
