# -*- coding:utf-8 -*-


class Clearer:
    def clearZero(self, mat, n):
        # write code here
        m = len(mat)
        n = 0 if m == 0 else len(mat[0])
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    mat[i][j] = 0
        return mat


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [
                    [1,2,3],
                    [0,1,2],
                    [0,0,1]
                ],
                3
            ),
            [
                [0,0,3],
                [0,0,0],
                [0,0,0]
            ]
        )
    ]
    test(Clearer().clearZero, test_data)
