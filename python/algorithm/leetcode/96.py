from collections import defaultdict


class Solution(object):
    def recursive(self, left, right):
        if left > right:
            return 1
        nums = self.table.get((left, right), None)
        if nums is not None:
            return nums
        nums = 0
        for i in range(left, right+1):
            left_children = self.recursive(left, i-1)
            right_children = self.recursive(i+1, right)
            nums += left_children * right_children
        self.table[(left, right)] = nums
        return nums

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.table = dict()
        if n == 0:
            return 0
        return self.recursive(1, n)
        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            3,
            5
        ),
        (
            0,
            0
        ),
        (
            20,
            6564120420
        )
    ]
    test(Solution().numTrees, test_data)

