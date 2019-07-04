from data_structure import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        print(root)
        ans = []
        n = root
        stack = [None]
        new = True
        while n:
            if new and n.left:
                stack.append(n)
                n = n.left
                continue

            ans.append(n.val)

            if n.right:
                n = n.right
                new = True
            else:
                n = stack.pop()
                new = False

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
