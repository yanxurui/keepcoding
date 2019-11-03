# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://leetcode.com/problems/delete-node-in-a-bst/discuss/93296/Recursive-Easy-to-Understand-Java-Solution/97795
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                rightMin = root.right
                while rightMin.left:
                    rightMin = rightMin.left
                rightMin.left = root.left
                return root.right



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([5,3,6,2,4,None,7]),
                3
            ),
            TreeNode.create([5,4,6,2,None,None,7])
        ),
        (
            (
                TreeNode.create([2,1,3]),
                4
            ),
            TreeNode.create([2,1,3])
        ),
        (
            (
                TreeNode.create([1]),
                1
            ),
            TreeNode.create([])
        ),
    ]
    test(Solution().deleteNode, test_data)

