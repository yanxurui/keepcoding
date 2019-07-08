#https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution

from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        root = None
        if inorder:
            v = postorder.pop(-1)
            root = TreeNode(v)
            i = inorder.index(v)
            root.right = self.buildTree(inorder[i+1:], postorder)
            root.left = self.buildTree(inorder[:i], postorder)
        return root


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [9,3,15,20,7],
                [9,15,7,20,3]
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

