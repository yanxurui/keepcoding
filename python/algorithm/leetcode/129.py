# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from common import TreeNode

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)
        
    def dfs(self, root, val):
        if root is None:
            return 0
        val = 10 * val + root.val
        if root.left is None and root.right is None:
            return val
        return self.dfs(root.left, val) + self.dfs(root.right, val)


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                TreeNode.create([1,2,3])
            ),
            25
        ),
        (
            (
                TreeNode.create([4,9,0,5,1])
            ),
            1026
        )
    ]
    test(Solution().sumNumbers, test_data)
