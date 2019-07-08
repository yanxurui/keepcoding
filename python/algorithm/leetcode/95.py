from common import TreeNode, unordered_equal


class Solution(object):
    def recursive(self, left, right):
        trees = []
        if left > right:
            return []
        for i in range(left, right+1):
            left_children = self.recursive(left, i-1)
            if not left_children:
                left_children = [None]
            right_children = self.recursive(i+1, right)
            if not right_children:
                right_children = [None]
            for left_child in left_children:
                for right_child in right_children:
                    t = TreeNode(i)
                    t.left = left_child
                    t.right = right_child
                    trees.append(t)
        return trees

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.recursive(1, n)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            3,
            [
                TreeNode.create([1,None,3,2]),
                TreeNode.create([3,2,None,1]),
                TreeNode.create([3,1,None,None,2]),
                TreeNode.create([2,1,3]),
                TreeNode.create([1,None,2,None,3])
            ]
        ),
        (
            2,
            [
                TreeNode.create([1,None,2]),
                TreeNode.create([2,1]),
            ]
        ),
        (
            0,
            []
        )
    ]
    test(Solution().generateTrees, test_data, compare=unordered_equal)

