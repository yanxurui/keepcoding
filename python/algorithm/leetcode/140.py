# https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways

class Solution(object):
    def backtrack(self, tab, res, tmp, i):
        for j in range(i):
            if tab[i][j] is not None:
                tmp.append(tab[i][j])
                if j > 0:
                    self.backtrack(tab, res, tmp, j)
                else:
                    res.append(' '.join(tmp[::-1]))
                tmp.pop()

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        tab = [[]]
        for i in range(1, n+1):
            tmp = []
            for j in range(i):
                if s[j:i] in wordDict:
                    tmp.append(s[j:i])
                else:
                    tmp.append(None)
            tab.append(tmp)
        res = []
        self.backtrack(tab, res, [], n)
        return res


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        # (
        #     (
        #         "catsanddog",
        #         ["cat", "cats", "and", "sand", "dog"]
        #     ),
        #     [
        #         "cats and dog",
        #         "cat sand dog"
        #     ]
        # ),
        # (
        #     (
        #         "pineapplepenapple",
        #         ["apple", "pen", "applepen", "pine", "pineapple"]
        #     ),
        #     [
        #         "pine apple pen apple",
        #         "pineapple pen apple",
        #         "pine applepen apple"
        #     ]
        # ),
        # (
        #     (
        #         "catsandog",
        #         ["cats", "dog", "sand", "and", "cat"]
        #     ),
        #     []
        # ),
        (
            (
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
            ),
            []
        )
    ]
    test(Solution().wordBreak, test_data, compare=unordered_equal)
