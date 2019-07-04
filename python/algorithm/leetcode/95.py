from common import unordered_equal


class Solution(object):
    def recursive(self, left, right):
        trees = []
        if left > right:
            return [[None]]
        for i in range(left, right+1):
            left_children = self.recursive(left, i-1)                
            right_children = self.recursive(i+1, right)
            for left_child in left_children:
                for right_child in right_children:
                    t = [i]
                    t += left_child
                    t += right_child
                    while t[-1] is None:
                        t.pop()
                    # translate from In-order traversal to by layer ??
                    trees.append(t)
        return trees

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        trees = self.recursive(1, n)
        return trees


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
