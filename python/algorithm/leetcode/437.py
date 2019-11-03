# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.rst = 0
        prev_sum = defaultdict(int)
        prev_sum[0] = 1
        self.traverse(root, prev_sum, 0, sum)
        return self.rst

    def traverse(self, root, prev_sum, cum_sum, target):
        if not root:
            return
        cum_sum += root.val
        self.rst += prev_sum[cum_sum-target]
        prev_sum[cum_sum] += 1
        self.traverse(root.left, prev_sum, cum_sum, target)
        self.traverse(root.right, prev_sum, cum_sum, target)
        prev_sum[cum_sum] -= 1



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([10,5,-3,3,2,None,11,3,-2,None,1]),
                8
            ),
            3
        )
    ]
    test(Solution().pathSum, test_data)

