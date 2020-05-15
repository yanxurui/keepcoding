# https://leetcode.com/problems/longest-string-chain/discuss/294890/C%2B%2BJavaPython-DP-Solution
from typing import List
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words.sort(key=len)
        for w in words:
            for i in range(len(w)):
                dp[w] = max(dp[w], dp[w[:i]+w[i+1:]]+1)
        return max(dp.values())


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ["a","b","ba","bca","bda","bdca"],
            4
        )
    ]
    test(Solution().longestStrChain, test_data)

