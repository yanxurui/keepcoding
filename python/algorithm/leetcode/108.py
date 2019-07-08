from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        else:
            mid = l//2
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [-10,-3,0,5,9],
            TreeNode.create([0,-3,9,-10,None,5])
        ),
        (
            [],
            None
        )
    ]
    test(Solution().sortedArrayToBST, test_data)

