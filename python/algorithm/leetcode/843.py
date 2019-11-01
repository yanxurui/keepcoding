# https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from collections import defaultdict

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        n = 0
        while n < 6:
            w = self.minmax(wordlist)
            n = master.guess(w)
            # keep words that match w with n chars
            wordlist = [w2 for w2 in wordlist if self.match(w2, w) == n]

    def match(self, w1, w2):
        assert len(w1) == len(w2)
        count = 0
        for i in range(len(w1)):
            if w1[i] == w2[i]:
                count += 1
        return count
    def minmax(self, wordlist):
        count = defaultdict(int)
        for i in range(len(wordlist)):
            w1 = wordlist[i]
            for j in range(i+1, len(wordlist)):
                w2 = wordlist[j]
                if self.match(w1, w2) == 0:
                    count[w1] += 1
                    count[w2] += 1
        return min(wordlist, key=lambda w:count[w])


