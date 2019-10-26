# -*- coding:utf-8 -*-

class SubMatrix:
    def maxSubMatrix(self, mat, n):
        # write code here
        rst = 1
        above = [[0 for j in range(n)] for i in range(n)]
        left = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                above[i][j] = 1
                left[i][j] = 1
                if i > 0 and mat[i][j] == mat[i-1][j]:
                    above[i][j] += above[i-1][j]
                if j > 0 and mat[i][j] == mat[i][j-1]:
                    left[i][j] += left[i][j-1]
                k = min(left[i][j], above[i][j])
                for l in range(k, 1, -1):
                    if above[i][j-l+1] >= l and left[i-l+1][j] >= l:
                        rst = max(rst, l)
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                [
                    [1,1,1],
                    [1,0,1],
                    [1,1,1]
                ],
                3
            ),
            3
        )
    ]
    test(SubMatrix().maxSubMatrix, test_data)
