# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.m = 0
        self.depth(root)
        return self.m

    def depth(self, root):
        # # of nodes in the path
        if root is None:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        if l + r > self.m:
            self.m = l + r
        return max(l, r) + 1


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([1,2,3,4,5]),
            3
        )
    ]
    test(Solution().diameterOfBinaryTree, test_data)

