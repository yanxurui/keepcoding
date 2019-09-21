# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization

from common import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
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
                p = p.right
            else:
                p = stack.pop()
                p = p.left
        return res[::-1]



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (TreeNode.create([1,None,2,3])),
            [3,2,1]
        )
    ]
    test(Solution().postorderTraversal, test_data)

