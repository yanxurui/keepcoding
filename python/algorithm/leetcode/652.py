# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://leetcode.com/problems/find-duplicate-subtrees/discuss/106020/Python-easy-understand-solution
from typing import List
from collections import defaultdict
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        d = defaultdict(list)
        self.traverse(root, d)
        rst = []
        for k, l in d.items():
            if len(l) > 1:
                rst.append(l[0])
        return rst

    def traverse(self, root, d):
        if root is None:
            return 'null'
        else:
            serialize = '%s,%s,%s' % (root.val, self.traverse(root.left, d), self.traverse(root.right, d))
            d[serialize].append(root)
            return serialize



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([1,2,3,4,None,2,4,None,None,4]),
            [
                TreeNode.create([4]),
                TreeNode.create([2,4]),
            ]
        )
    ]
    test(Solution().findDuplicateSubtrees, test_data)

