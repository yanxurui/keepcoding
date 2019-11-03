# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        self.traverse(root)
        return self.moves
    def traverse(self, root):
        # post order traverse
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.moves = self.moves + abs(left) + abs(right)
        return left + right + root.val-1

if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([3,0,0]),
            2
        ),
        (
            TreeNode.create([0,3,0]),
            3
        ),
        (
            TreeNode.create([1,0,2]),
            2
        ),
        (
            TreeNode.create([1,0,0,None,3]),
            4
        ),
    ]
    test(Solution().distributeCoins, test_data)

