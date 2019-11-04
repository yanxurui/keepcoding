# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left or root.right:
            assert root.left and root.right
            l = root.left.val
            r = root.right.val
            if root.val == root.left.val:
                l = self.findSecondMinimumValue(root.left)
            if root.val == root.right.val:
                r = self.findSecondMinimumValue(root.right)
            if l!=-1 and r!=-1:
                return min(l, r)
            elif l == -1:
                return r
            else:
                return l
        else:
            return -1


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([2,2,5,None,None,5,7]),
            5
        ),
        (
            TreeNode.create([2,2,2]),
            -1
        ),
        (
            TreeNode.create(
                [1,
                1,3,
              1,1,3,4,
          3,1,1,1,3,8,4,8,
      3,3,1,6,2,1]),
            2
        ),
    ]
    test(Solution().findSecondMinimumValue, test_data)

