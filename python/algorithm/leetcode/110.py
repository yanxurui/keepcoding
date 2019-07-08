from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root):
        if root is None:
            return 0, True
        else:
            ld, lb = self.dfs(root.left)
            rd, rb = self.dfs(root.right)
            return max(ld, rd)+1, lb and rb and not abs(ld-rd)>1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        d, b = self.dfs(root)
        return b


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([3,9,20,None,None,15,7]),
            True
        ),
        (
            TreeNode.create([1,2,2,3,3,None,None,4,4]),
            False
        )
    ]
    test(Solution().isBalanced, test_data)

