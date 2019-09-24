# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self._p = root
        self._stack = []
        if self._p is not None:
            while self._p.left:
                self._stack.append(self._p)
                self._p = self._p.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        res = self._p.val
        if self._p.right:
            self._p = self._p.right
            while self._p.left:
                self._stack.append(self._p)
                self._p = self._p.left
        else:
            if self._stack:
                self._p = self._stack.pop()
            else:
                self._p = None
        return res

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self._p != None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    root = TreeNode.create([7,3,15,None,None,9,20])
    iterator = BSTIterator(root);
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    assert iterator.hasNext() == True
    assert iterator.next() == 15
    assert iterator.hasNext() == True
    assert iterator.next() == 20
    assert iterator.hasNext() == False
