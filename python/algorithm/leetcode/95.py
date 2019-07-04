from copy import deepcopy
from common import TreeNode, unordered_equal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recursive(self, left, right):
        trees = []
        if left > right:
            return [None]
        for i in range(left, right+1):
            node = TreeNode(i)
            left_children = self.recursive(left, i-1)                
            right_children = self.recursive(i+1, right)
            for left_child in left_children:
                node.left = left_child
                for right_child in right_children:
                    node.right = right_child
                    trees.append(deepcopy(node))
        return trees

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        ans = []
        import pdb
        # pdb.set_trace()
        trees = self.recursive(1, n)
        for tree in trees:
            ans.append(tree.to_list())
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            3,
            [
                [1,None,3,2],
                [3,2,None,1],
                [3,1,None,None,2],
                [2,1,3],
                [1,None,2,None,3]
            ]
        ),
        (
            2,
            [
                [1,None,2],
                [2,1],
            ]
        ),
    ]
    test(Solution().generateTrees, test_data, compare=unordered_equal)
