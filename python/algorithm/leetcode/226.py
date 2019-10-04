# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (TreeNode.create([4, 2,7, 1,3, 6,9, None, None, None, None, None, None, None, None])),
            TreeNode.create([4, 7,2, 9,6, 3,1, None, None, None, None, None, None, None, None])
        )
    ]
    test(Solution().invertTree, test_data)
