# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # in-order traverse
        rst = 0
        stack = []
        cur =root
        while True:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                if stack:
                    cur = stack.pop()
                    if L <= cur.val <= R:
                        rst += cur.val
                    cur = cur.right
                else:
                    break
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([10,5,15,3,7,None,18]),
                7,15
            ),
            32
        ),
        (
            (
                TreeNode.create([10,5,15,3,7,13,18,1,None,6]),
                6,10
            ),
            23
        ),
    ]
    test(Solution().rangeSumBST, test_data)

