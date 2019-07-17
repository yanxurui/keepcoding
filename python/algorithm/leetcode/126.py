class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        ans = []
        self.dfs(beginWord, endWord, wordList, [beginWord], ans)
        return ans

    def dfs(self, b, e, words, tmp, ans):

        if b == e:
            if ans and len(tmp) < len(ans[0]):
                ans.clear()
            ans.append(list(tmp))
            return
        for i, w in enumerate(words):
            if w in tmp:
                continue
            d = 0
            for i in range(len(b)):
                if b[i] != w[i]:
                    d += 1
                    if d > 1:
                        break
            if d == 1:
                if ans and len(tmp)+1 > len(ans[0]):
                    continue
                tmp.append(w)
                self.dfs(w, e, words, tmp, ans)
                tmp.pop()


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
        ),
        (
            (
                "qa",
                "sq",
                ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
            ),
            [
                ["hot","hog","dog"],
                ["hot","dot","dog"],
            ]
        )
    ]
    test(Solution().findLadders, test_data, compare=unordered_equal)
