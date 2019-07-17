from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, ans, root, tmp, acc, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            # reach leaf
            if root.val + acc == sum:
                ans.append(tmp+[root.val])
        else:
            tmp.append(root.val)
            acc += root.val
            ret = self.dfs(ans, root.left, tmp, acc, sum) or self.dfs(ans, root.right, tmp, acc, sum)
            tmp.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        ans = []
        self.dfs(ans, root, [], 0, sum)
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                TreeNode.create([5,4,8,11,None,13,4,7,2,None,None,5,1]),
                22
            ),
            [
               [5,4,11,2],
               [5,8,4,5]
            ]
        ),
    ]
    test(Solution().pathSum, test_data)

