# https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first, self.second = None, None
        self.prev = TreeNode(float('-inf'))
        self.in_order(root)

        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp

    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.left)

        if root.val < self.prev.val:
            if self.first is None:
                self.first = self.prev
            self.second = root

        self.prev = root
        self.in_order(root.right)

def wrapper(root):
    Solution().recoverTree(root)
    return root


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([1,3,None,None,2]),
            TreeNode.create([3,1,None,None,2]),
        ),
        (
            TreeNode.create([3,1,4,None,None,2]),
            TreeNode.create([2,1,4,None,None,3]),
        )
    ]
    test(wrapper, test_data)

