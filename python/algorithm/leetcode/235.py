# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        self.traverse(root, p, path1)
        self.traverse(root, q, path2)

        for i, (n1,n2) in enumerate(zip(path1, path2)):
            if n1 != n2:
                break
            if n1 == p or n1 == q:
                i += 1
                break
        return path1[i-1]

    def traverse(self, root, v, res):
        if not root:
            return False
        res.append(root)
        if root == v:
            return True
        else:
            if self.traverse(root.left, v, res) or self.traverse(root.right, v, res):
                return True
            else:
                res.pop()
                return False


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
