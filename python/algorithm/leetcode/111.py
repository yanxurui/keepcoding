from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([3,9,20,None,None,15,7]),
            2
        ),
        (
            TreeNode.create([]),
            0
        ),
        (
            TreeNode.create([1,2]),
            2
        ),
    ]
    test(Solution().minDepth, test_data)

