# https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.dfs(p, q)
        
    def dfs(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        return t1.val == t2.val and self.dfs(t1.left, t2.left) and self.dfs(t1.right, t2.right)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                TreeNode.create([1,2,3]),
                TreeNode.create([1,2,3])
            ),
            True
        ),
        (
            (
                TreeNode.create([1,2]),
                TreeNode.create([1,None,2])
            ),
            False
        ),
        (
            (
                TreeNode.create([1,2,1]),
                TreeNode.create([1,1,2])
            ),
            False
        )
    ]
    test(Solution().isSameTree, test_data)

