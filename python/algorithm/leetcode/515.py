# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        level = [root]
        rst = []
        while level:
            l = len(level)
            tmp = level[0].val
            for i in range(l):
                cur = level.pop(0)
                if cur.val > tmp:
                    tmp = cur.val
                if cur.left:
                    level.append(cur.left)
                if cur.right:
                    level.append(cur.right)
            rst.append(tmp)
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([1,3,2,5,3,None,9]),
            [1,3,9]
        )
    ]
    test(Solution().largestValues, test_data)

