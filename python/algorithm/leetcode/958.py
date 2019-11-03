# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque([root])
        while q:
            cur = q.popleft()
            if cur is None:
                return not any(q) # all are None
            else:
                q.append(cur.left)
                q.append(cur.right)


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([1,2,3,4,5,6]),
            True
        ),
        (
            TreeNode.create([1,2,3,4,5,None,7]),
            False
        ),
    ]
    test(Solution().isCompleteTree, test_data)

