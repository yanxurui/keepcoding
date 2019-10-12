# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64963/3-lines-with-O(1)-space-1-Liners-Alternatives

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    root = TreeNode.create([6,2,8,0,4,7,9,None,None,3,5])
    root2 = TreeNode.create([2,1, None, None, None])
    test_data = [
        (
            (
                root,
                root.left, root.right
            ),
            root
        ),
        (
            (
                root,
                root.left, root.left.right
            ),
            root.left
        ),
        (
            (
                root,
                root.left.left, root.right.right
            ),
            root
        ),
        (
            (
                root2,
                root2, root2.left
            ),
            root2
        )
    ]
    test(Solution().lowestCommonAncestor, test_data)
