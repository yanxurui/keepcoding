# -*- coding:utf-8 -*-
class Transform:
    def transformImage(self, mat, n):
        # write code here
        for i in range(n/2):
            for j in range(i, n-i-1):
                tmp = mat[i][j]
                mat[i][j] = mat[n-j-1][i]
                mat[n-j-1][i] = mat[n-i-1][n-j-1]
                mat[n-i-1][n-j-1] = mat[j][n-i-1]
                mat[j][n-i-1] = tmp
        return mat


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [
                    [1,2,3],
                    [4,5,6],
                    [7,8,9]
                ],
                3
            ),
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ]
        )
    ]
    test(Transform().transformImage, test_data)
