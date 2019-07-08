from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, tmp, acc, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            # reach leaf
            if root.val + acc == sum:
                return True
            else:
                return False
        else:
            tmp.append(root.val)
            acc += root.val
            ret = self.dfs(root.left, tmp, acc, sum) or self.dfs(root.right, tmp, acc, sum)
            tmp.pop()
            return ret

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, [], 0, sum)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                TreeNode.create([5,4,8,11,None,13,4,7,2,None,None,None,None,1]),
                22
            ),
            True
        ),
        (
            (
                TreeNode.create([1,2]),
                1
            ),
            False
        ),
        (
            (
                TreeNode.create([-2,None,-3]),
                -5
            ),
            True
        ),
    ]
    test(Solution().hasPathSum, test_data)

