import sys
from typing import List
from collections import defaultdict

INT_MAX = sys.maxsize


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.dic = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.dic[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = INT_MAX
        l1, l2 = self.dic[word1], self.dic[word2]
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


if __name__ == '__main__':
    wordDistance = WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
    assert wordDistance.shortest("coding", "practice") == 3
    assert wordDistance.shortest("makes", "coding") == 1
