# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        cur = root
        while True:
            if val > cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    break
        return root


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([4,2,7,1,3]),
                5
            ),
            TreeNode.create([4,2,7,1,3,5])
        )
    ]
    test(Solution().insertIntoBST, test_data)

