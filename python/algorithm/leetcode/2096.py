from typing import Optional
from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search(self, root, t, path):
        if root is None:
            return False
        if root.val == t:
            return True
        if self.search(root.left, t, path):
            path.append('L')
            return True
        elif self.search(root.right, t, path):
            path.append('R')
            return True
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # step 1: find the path from root to the start and dest node respectively
        start = []
        dest = []
        self.search(root, startValue, start)
        self.search(root, destValue, dest)
        start = start[::-1]
        dest = dest[::-1]
        # step 2: remove the common prefix
        i = 0
        while i < len(start) and i < len(dest) and start[i] == dest[i]:
            i += 1
        # step 3:
        return 'U'*(len(start)-i) + ''.join(dest[i:])

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                TreeNode.create([5,1,2,3,None,6,4]),
                3,
                6
            ),
            'UURL'
        ),
        (
            (
                TreeNode.create([2,1]),
                2,
                1
            ),
            'L'
        ),
    ]
    test(Solution().getDirections, test_data)

