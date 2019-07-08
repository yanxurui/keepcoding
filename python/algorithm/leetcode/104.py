from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([3,9,20,None,None,15,7]),
            3
        ),
        (
            None,
            0
        )
    ]
    test(Solution().maxDepth, test_data)

