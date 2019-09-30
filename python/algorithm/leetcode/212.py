from collections import defaultdict

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isWord = False
        self.children = defaultdict(lambda: None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self
        for c in word:
            if p.children[c] is None:
                p.children[c] = Trie()
            p = p.children[c]
        p.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = set([])
        T = Trie()
        for w in words:
            T.insert(w)
        m = len(board)
        n = len(board[0])
        mask = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.findChar(board, mask, T, i, j, [], res)
        return list(res)

    def findChar(self, board, mask, T, i, j, tmp, res):
        if not (i >= 0 and i < len(board) and j >=0 and j < len(board[0])):
            return
        if mask[i][j]:
            return
        c = board[i][j]
        mask[i][j] = True
        T = T.search(c)
        if T:
            tmp = tmp+[c]
            if T.isWord:
                res.add(''.join(tmp))
            self.findChar(board, mask, T, i-1, j, tmp, res)
            self.findChar(board, mask, T, i+1, j, tmp, res)
            self.findChar(board, mask, T, i, j-1, tmp, res)
            self.findChar(board, mask, T, i, j+1, tmp, res)
        mask[i][j] = False


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                [
                  ['o','a','a','n'],
                  ['e','t','a','e'],
                  ['i','h','k','r'],
                  ['i','f','l','v']
                ],
                ["oath","pea","eat","rain"]
            ),
            ["eat","oath"]
        ),
        (
            (
                [["a","a"]],
                ["a"]
            ),
            ["a"]
        ),
        (
            (
                [
                    ["a","b"],
                    ["a","a"]
                ],
                ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
            ),
            ["aaa","aaab","aaba","aba","baa"]
        ),
    ]
    test(Solution().findWords, test_data, compare=unordered_equal)
