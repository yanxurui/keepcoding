# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        rst = []
        self.recursive(root, [], rst)
        return rst

    def recursive(self, root, path, rst):
        path.append(root.val)
        if not root.left and not root.right:
            # leaf node
            rst.append('->'.join(map(str,path)))
        else:
            if root.left:
                self.recursive(root.left, path, rst)
            if root.right:
                self.recursive(root.right, path, rst)
        path.pop()


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            TreeNode.create([1,2,3,None,5]),
            ["1->2->5", "1->3"]
        )
    ]
    test(Solution().binaryTreePaths, test_data)

