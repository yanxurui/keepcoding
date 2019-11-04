# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1 or root is None:
            node = TreeNode(v)
            node.left = root
            return node
        q = [root]
        depth = 0
        while q:
            depth += 1
            n = len(q)
            if depth == d-1:
                for i in range(n):
                    cur = q.pop(0)
                    l = TreeNode(v)
                    l.left = cur.left
                    cur.left = l
                    r = TreeNode(v)
                    r.right = cur.right
                    cur.right = r
                break
            else:
                for i in range(n):
                    cur = q.pop(0)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
        return root


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            (
                TreeNode.create([4,2,6,3,1,5]),
                1, 2
            ),
            TreeNode.create([4,1,1,2,None,None,6,3,1,5])
        ),
        (
            (
                TreeNode.create([4,2,None,3,1]),
                1, 3
            ),
            TreeNode.create([4,2,None,1,1,3,None,None,1])
        )
    ]
    test(Solution().addOneRow, test_data)

