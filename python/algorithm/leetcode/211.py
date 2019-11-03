from collections import defaultdict

class Node(object):
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(lambda: None)

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.isWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchUtil(self.root, word)

    def searchUtil(self, root, word):
        if not word:
            return root.isWord
        p = root
        c = word[0]
        if c == '.':
            for k,v in p.children.items():
                if self.searchUtil(v, word[1:]):
                    return True
            return False
        else:
            if c not in p.children:
                return False
            else:
                return self.searchUtil(p.children[c], word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    # assert obj.search("pad") == False
    # assert obj.search("bad") == True
    # assert obj.search(".ad") == True
    # assert obj.search("b..") == True
    assert obj.search("b.") == False
