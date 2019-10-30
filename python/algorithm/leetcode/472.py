# https://leetcode.com/problems/concatenated-words/discuss/95652/Java-DP-Solution
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key=lambda w: len(w))
        dic = set()
        rst = []
        for w in words:
            if self.canForm(w, dic):
                rst.append(w)
            dic.add(w)
        return rst

    def canForm(self, w, dic):
        if len(dic) == 0:
            return False
        dp = [False] * (len(w)+1)
        dp[0] = True
        for i in range(1, len(w)+1):
            for j in range(i):
                if dp[j] and w[j:i] in dic:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
            ["catsdogcats","dogcatsdog","ratcatdogcat"]
        ),
        (
            ['a', 'ab', 'c', 'abc'],
            ['abc']
        ),
        (
            [""],
            []
        ),
    ]
    test(Solution().findAllConcatenatedWordsInADict, test_data, compare=unordered_equal)

