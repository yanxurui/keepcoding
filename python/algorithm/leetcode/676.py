from typing import List
from string import ascii_lowercase
class Node:
    def __init__(self):
        self.isWord = False
        self.children = {}
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for w in dict:
            cur = self.root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        cur = self.root
        for i in range(len(word)):
            for c in ascii_lowercase:
                if c == word[i]:
                    continue
                # replace
                new_word = word[:i] + c + word[i+1:]
                if self.searchUtil(new_word):
                    return True
        return False

    def searchUtil(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord



# https://leetcode.com/problems/implement-magic-dictionary/discuss/107446/Easy-14-lines-Java-solution-HashMap
from collections import defaultdict

class MagicDictionary2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = defaultdict(list)
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for w in dict:
            for i in range(len(w)):
                k = w[:i]+w[i+1:]
                self.dictionary[k].append((i, w[i]))
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for i in range(len(word)):
            k = word[:i] + word[i+1:]
            for j,c in self.dictionary[k]:
                if j == i and c != word[i]:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary2()
obj.buildDict(["hello", "leetcode"])
assert obj.search("hello") is False
assert obj.search("hhllo")
assert obj.search("hell") is False
assert obj.search("leetcoded") is False