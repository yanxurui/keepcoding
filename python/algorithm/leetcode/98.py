from common import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import sys

INT_MAX = sys.maxsize

class Solution(object):
    def recursive(self, root, l, r):
        if root is None:
            return True
        if l < root.val < r:
            if self.recursive(root.left, l, root.val) and self.recursive(root.right, root.val, r):
                return True
        return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursive(root, -INT_MAX, INT_MAX)

class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        pre = None
        while root or stack:
            # push left
            while root:
                stack.append(root)
                root = root.left
            p = stack.pop()
            if pre and pre.val >= p.val:
                return False
            else:
                pre = p
            root = p.right
        return True


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
        ),
        (
            TreeNode.create([1, 1]),
            False
        )
    ]
    test(Solution2().isValidBST, test_data)

