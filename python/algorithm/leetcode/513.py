# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# left side view
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = []
        self.util(root, q, 0)
        return q[-1]

    def util(self, root, q, level):
        if root:
            if len(q) == level:
                q.append(root.val)
            self.util(root.left, q, level+1)
            self.util(root.right, q, level+1)

# layer by layer, from right to left
from collections import deque
class Solution2:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur.right:
                q.append(cur.right)
            if cur.left:
                q.append(cur.left)
        return cur.val


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([2,1,3]),
            1
        ),
        (
            TreeNode.create([1,2,3,4,None,5,6,None,None,7]),
            7
        ),
    ]
    test(Solution2().findBottomLeftValue, test_data)

