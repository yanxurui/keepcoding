# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return root
        else:
            if root.val < L:
                return self.trimBST(root.right, L, R)
            elif root.val > R:
                return self.trimBST(root.left, L, R)
            else:
                root.left = self.trimBST(root.left, L, R)
                root.right = self.trimBST(root.right, L, R)
                return root



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([1,0,2]),
                1,2
            ),
            TreeNode.create([1,None,2])
        ),
        (
            (
                TreeNode.create([3,0,4,None,2,None,None,1]),
                1,3
            ),
            TreeNode.create([3,2,None,1])
        ),
    ]
    test(Solution().trimBST, test_data)

