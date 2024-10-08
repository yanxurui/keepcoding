from common import TreeNode
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            p = root.left
            while p.right:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None

# iterative
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        head = prev = TreeNode(0)
        # traverse in pre-order
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                cur.left = None
                prev.right = cur
                prev = cur
        return head.right


def wrapper(root):
    Solution2().flatten(root)
    return root


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([1,2,5,3,4,None,6]),
            TreeNode.create([1,None,2,None,3,None,4,None,5,None,6])
        ),
    ]
    test(wrapper, test_data)

