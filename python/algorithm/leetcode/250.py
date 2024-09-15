# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from common import TreeNode

class Solution:
    def checkUnival(self, root):
        if root is None:
            return True
        l = self.checkUnival(root.left)
        r = self.checkUnival(root.right)
        if l and r:
            if (root.left and root.left.val != root.val) or (root.right and root.right.val != root.val):
                return False
            else:
                self.count += 1
                return True
        else:
            return False

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.checkUnival(root)
        return self.count


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([5,1,5,5,5,None,5]),
            4
        ),
        (
            TreeNode.create([]),
            0
        ),
        (
            TreeNode.create([5,5,5,5,5,None,5]),
            6
        ),
    ]
    test(Solution().countUnivalSubtrees, test_data)

