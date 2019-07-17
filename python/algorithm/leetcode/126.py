# https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer

from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        # BFS layer by layer
        while layer:
            newlayer = defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww] += [l+[neww] for l in layer[w]]
            wordList -= set(newlayer.keys())
            layer = newlayer
        return res


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            (
                "hit",
                "cog",
                ["hot","dot","dog","lot","log","cog"]
            ),
            [
              ["hit","hot","dot","dog","cog"],
              ["hit","hot","lot","log","cog"]
            ]
        ),
        (
            (
                "hit",
                "cog",
                ["hot","dot","dog","lot","log",]
            ),
            []
        ),
        (
            (
                "hot",
                "dog",
                ["hot","cog","dog","tot","hog","hop","pot","dot"]
            ),
            [
                ["hot","hog","dog"],
                ["hot","dot","dog"],
            ]
        )
    ]
    test(Solution().findLadders, test_data, compare=unordered_equal)
