from typing import Optional
from common import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None:
            return root
        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return newRoot


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([1,2,3,4,5]),
            TreeNode.create([4,5,2,None,None,3,1])
        ),
        (
            TreeNode.create([]),
            TreeNode.create([])
        ),
        (
            TreeNode.create([1]),
            TreeNode.create([1])
        ),
    ]
    test(Solution().upsideDownBinaryTree, test_data)

