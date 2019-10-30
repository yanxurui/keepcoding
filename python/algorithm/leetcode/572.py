# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.equal(s, t):
            return True
        if s:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return False

    def equal(self, s, t):
        if s is None or t is None:
            return s == t
        if s.val != t.val:
            return False
        return self.equal(s.left, t.left) and self.equal(s.right, t.right)


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([3,4,5,1,2]),
                TreeNode.create([4,1,2])
            ),
            True
        ),
        (
            (
                TreeNode.create([3,4,5,1,2,None,None,None,None,0]),
                TreeNode.create([4,1,2])
            ),
            False
        ),
        (
            (
                TreeNode.create([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2]),
                TreeNode.create([1,None,1,None,1,None,1,None,1,None,1,2])
            ),
            True
        ),
    ]
    test(Solution().isSubtree, test_data)

