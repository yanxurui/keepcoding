# -*- coding:utf-8 -*-



class Trie:
    def __init__(self, s=None):
        self.isWord = False
        self.d = dict()
        if s is not None:
            if s == '':
                self.isWord = True
            else:
                self.d[s[0]] = Trie(s[1:])

    def insert(self, s):
        if s == '':
            self.isWord = True
        else:
            c = s[0]
            sub = self.d.get(s[0], None)
            if sub:
                sub.insert(s[1:])
            else:
                self.d[s[0]] = Trie(s[1:])

    def prefix(self, s):
        if s == '':
            return self.isWord
        cur = self
        for i, c in enumerate(s):
            sub = cur.d.get(c, None)
            if sub:
                cur = sub
            else:
                return 0
            if cur.isWord:
                return i+1 # the first i+1 chars in s appears in the tree

    def find(self, s):
        if s == '':
            return self.isWord
        sub = self.d.get(s[0], None)
        if not sub:
            return False
        return sub.find(s[1:])

    def delete(self, s):
        if s == '' and self.isWord:
            self.isWord = False
            return
        cur = self
        stack = []
        for c in s:
            sub = cur.d.get(c, None)
            if sub:
                stack.append((cur, c))
                cur = sub
            else:
                return
        if cur.isWord:
            # find
            cur.isWord = False
            # no subtree
            while stack:
                cur, c = stack.pop()
                if cur.isWord:
                    break
                if not cur.d[c].d:
                    # no subtree
                    del cur.d[c]
                else:
                    break


class Substr:
    def chkSubStr(self, p, n, s):
        # write code here
        d = {}
        root = Trie()
        for w in p:
            root.insert(w)
        import pdb
        # pdb.set_trace()
        for i in range(len(s)):
            while True:
                j = root.prefix(s[i:i+8])
                if j > 0:
                    w = s[i:i+j]
                    d[w] = True
                    root.delete(w)
                else:
                    break
        return [d.get(w, False) for w in p]



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                ["a","b","c","d"],4,"abc"
            ),
            [True,True,True,False]
        ),
        (
            (
                ["a","ab","abc","d"],4,"abc"
            ),
            [True,True,True,False]
        ),
        (
            (
                ["bav","yacv","wez","p","zei","m","ypx","oqlz","by","tudp","vcwb","bwkw","tjc","hs","gbjg","c","qmfe","wvc","cw"],19,"bwkwby"
            ),
            [False,False,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False]
        ),
    ]
    test(Substr().chkSubStr, test_data)
