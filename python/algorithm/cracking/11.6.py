# -*- coding:utf-8 -*-

class Finder:
    def findElement(self, mat, n, m, x):
        # write code here
        n, m = m, n
        i, j = 0, n-1
        while i < m and j >= 0:
            if x == mat[i][j]:
                return [i, j]
            elif x > mat[i][j]:
                i += 1
            else:
                j -= 1
        return -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [[1,2,3],[4,5,6]],2,3,6
            ),
            [1,2]
        )
    ]
    test(Finder().findElement, test_data)
