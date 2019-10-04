# https://leetcode.com/problems/count-complete-tree-nodes/discuss/61958/Concise-Java-solutions-O(log(n)2)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        if h < 0:
            return 0
        if self.height(root.right) == h - 1:
            return (1<<h) + self.countNodes(root.right)
        else:
            return (1<<(h-1)) + self.countNodes(root.left)

    def height(self, root):
        return -1 if root is None else 1+self.height(root.left)


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (TreeNode.create([1,2,3,4,5,6,None])),
            6
        )
    ]
    test(Solution().countNodes, test_data)
