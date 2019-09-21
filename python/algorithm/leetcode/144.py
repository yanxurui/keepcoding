from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        p = root
        while stack or p:
            if p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
        return res


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (TreeNode.create([1,None,2,3])),
            [1,2,3]
        )
    ]
    test(Solution().preorderTraversal, test_data)

