from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.m  = root.val
        self.dfs(root)
        return self.m

    def dfs(self, root):

        if root is None:
            return 0
        else:
            l = self.dfs(root.left)
            r = self.dfs(root.right)
            if l < 0:
                l = 0
            if r < 0:
                r = 0
            if root.val + l + r > self.m:
                self.m = root.val + l + r
            return root.val + max(l, r)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([1,2,3]),
            6
        ),
        (
            TreeNode.create([-10,9,20,None,None,15,7]),
            42
        ),
        (
            TreeNode.create([-3]),
            -3
        ),
        (
            TreeNode.create([1,-2,3]),
            4
        ),
        (
            TreeNode.create([5,4,8,11,None,13,4,7,2,None,None,None,1]),
            48
        ),
    ]
    test(Solution().maxPathSum, test_data)
