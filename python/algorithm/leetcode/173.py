# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from common import TreeNode

class BSTIterator:

    def __init__(self, root: TreeNode):
        self._stack = []
        self._pushLeft(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        assert len(self._stack) > 0
        node = self._stack.pop()
        self._pushLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self._stack) > 0

    def _pushLeft(self, node):
        while node is not None:
            self._stack.append(node)
            node = node.left

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
