from common import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursive(self, root, l, g):
        if root is None:
            return True
        if l:
            if not root.val < l:
                return False
        if g:
            if not root.val > g:
                return False
        if root.left:
            if not (root.left.val < root.val and self.recursive(root.left, l=root.val, g=g)):
                return False
        if root.right:
            if not (root.right.val > root.val and self.recursive(root.right, l=l, g=root.val)):
                return False
        return True
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursive(root, None, None)
        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([2,1,3]),
            True
        ),
        (
            TreeNode.create([5,1,4,None,None,3,6]),
            False
        ),
        (
            TreeNode.create([]),
            True
        ),
        (
            TreeNode.create([10,5,15,None,None,6,20]),
            False
        )
    ]
    test(Solution().isValidBST, test_data)

