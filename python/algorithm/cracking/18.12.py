# -*- coding:utf-8 -*-
INT_MIN = -(2<<31)

class SubMatrix:
    def sumOfSubMatrix(self, mat, n):
        # write code here
        rst = INT_MIN
        for i in range(n):
            tmp = [0] * n
            for j in range(i, n):
                for k in range(n):
                    tmp[k] += mat[j][k]
                rst = max(rst, self.maxSubArray(tmp))
        return rst

    def sumOfColumn(self, mat):
        # sum of each column in a matrix
        return [sum(col) for col in zip(*mat)]

    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        rst = INT_MIN
        prev = nums[0]
        for i in range(1, len(nums)):
            prev = max(0, prev) + nums[i]
            if prev > rst:
                rst = prev
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                [
                    [1,2,-3],
                    [3,4,-5],
                    [-5,-6,-7]
                ],3
            ),
            10
        ),
        (
            (
                [
                    [1,2],
                    [3,-2]
                ],
                2
            ),
            4
        ),
        (
            (
                [
                    [-1,-2],
                    [-3, 1]
                ],
                2
            ),
            1
        ),
    ]
    test(SubMatrix().sumOfSubMatrix, test_data)
