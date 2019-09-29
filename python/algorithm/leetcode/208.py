# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58832/AC-JAVA-solution-simple-using-single-array/60221

from collections import defaultdict

class Node(object):
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(lambda: None)

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for c in word:
            if p.children[c] is None:
                p.children[c] = Node()
            p = p.children[c]
        p.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app") 
    assert trie.search("app") == True

    trie.insert("appstore") 
    assert trie.startsWith("apps") == True
