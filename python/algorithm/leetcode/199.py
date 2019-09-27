# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rightView(root, 0, res)
        return res

    def rightView(self, root, depth, res):
        if root:
            if depth == len(res):
                res.append(root.val)
            self.rightView(root.right, depth+1, res)
            self.rightView(root.left, depth+1, res)


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (TreeNode.create([1,2,3,None,5,None,4])),
            [1,3,4]
        )
    ]
    test(Solution().rightSideView, test_data)
