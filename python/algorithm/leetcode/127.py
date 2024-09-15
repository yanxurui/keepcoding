from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        layer = set([beginWord])
        # BFS layer by layer
        n = 1
        while layer:
            newlayer = set()
            for w in layer:
                if w == endWord:
                    return n
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer.add(neww)
            wordList -= newlayer
            layer = newlayer
            n += 1
        return 0


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                "hit",
                "cog",
                ["hot","dot","dog","lot","log","cog"]
            ),
            5
        ),
        (
            (
                "hit",
                "cog",
                ["hot","dot","dog","lot","log",]
            ),
            0
        ),
        (
            (
                "hot",
                "dog",
                ["hot","cog","dog","tot","hog","hop","pot","dot"]
            ),
            3
        )
    ]
    test(Solution().ladderLength, test_data)
