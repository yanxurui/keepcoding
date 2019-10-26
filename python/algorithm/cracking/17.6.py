# -*- coding:utf-8 -*-

class Rearrange:
    def findSegment(self, A, n):
        # write code here
        if len(A) == 0:
            return [0, 0]
        left, right = 0, 0
        m = A[0]
        for i in range(n):
            if A[i] >= m:
                m = A[i]
            else:
                right = i
        m = A[-1]
        for i in range(n-1, -1, -1):
            if A[i] <= m:
                m = A[i]
            else:
                left = i
        return [left, right]



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,4,6,5,9,10],6
            ),
            [2, 3]
        ),
        (
            (
                [1,2,3,4],4
            ),
            [0, 0]
        ),
        (
            (
                [3,4,1,2],4
            ),
            [0, 3]
        ),
        (
            (
                [1,2,10,1,8,9],
                6
            ),
            [1, 5]
        ),
    ]
    test(Rearrange().findSegment, test_data)
