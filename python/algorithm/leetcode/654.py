# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.util(nums, 0, len(nums)-1)
    def util(self, nums, b, e):
        if b > e:
            return None
        m = nums[b]
        k = b
        for i in range(b+1, e+1):
            if nums[i] > m:
                m = nums[i]
                k = i
        root = TreeNode(m)
        root.left = self.util(nums, b, k-1)
        root.right = self.util(nums, k+1, e)
        return root


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            [3,2,1,6,0,5],
            TreeNode.create([6,3,5,None,2,0,None,None,1])
        )
    ]
    test(Solution().constructMaximumBinaryTree, test_data)

