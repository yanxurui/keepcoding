# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.

from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = None
        if inorder:
            v = preorder.pop(0)
            i = inorder.index(v)
            root = TreeNode(v)
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
        return root



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [3,9,20,15,7],
                [9,3,15,20,7]
            ),
            TreeNode.create([3,9,20,None,None,15,7])
        ),
        (
            (
                [],
                []
            ),
            None
        )
    ]
    test(Solution().buildTree, test_data)

