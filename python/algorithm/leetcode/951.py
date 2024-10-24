from typing import List, Optional
from common import TreeNode

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                if self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right):
                    return True
                if self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left):
                    return True
        return False

if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (
                TreeNode.create([1,2,3,4,5,6,None,None,None,7,8]),
                TreeNode.create([1,3,2,None,6,4,5,None,None,None,None,8,7])
            ),
            True
        ),
        (
            (
                TreeNode.create([]),
                TreeNode.create([])
            ),
            True
        ),
        (
            (
                TreeNode.create([]),
                TreeNode.create([1])
            ),
            False
        ),
        (
            (
                TreeNode.create([1,2,3,4,5,6,None,None,None,7,8]),
                TreeNode.create([1,3,2,None,6,4,5,None,None,None,None,8,7])
            ),
            True
        ),
    ]
    test(Solution().flipEquiv, test_data)
