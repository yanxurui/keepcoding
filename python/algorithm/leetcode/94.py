from common import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        cur = root
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([1,None,2,3]),
            [1,3,2]
        )
    ]
    test(Solution().inorderTraversal, test_data)
