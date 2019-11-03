# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        level = [(root, 0)]
        rst = 0
        while level:
            rst = max(rst, level[-1][1] - level[0][1])
            new_level = []
            for node, col in level:
                if node.left:
                    new_level.append((node.left, 2*col))
                if node.right:
                    new_level.append((node.right, 2*col+1))
            level = new_level
        return rst+1


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([1,3,2,5,3,None,9]),
            4
        ),
        (
            TreeNode.create([1,3,None,5,3]),
            2
        ),
        (
            TreeNode.create([1,3,2,5]),
            2
        ),
        (
            TreeNode.create([1,3,2,5,None,None,9,6,None,None,7]),
            8
        ),
        (
            TreeNode.create([1]),
            1
        ),
    ]
    test(Solution().widthOfBinaryTree, test_data)

