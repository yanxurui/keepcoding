# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        return self.bs(A, 0, n-1)

    def bs(self, A, b, e):
        if b > e:
            return False
        m = (b+e)/2
        if A[m] == m:
            return True
        elif A[m] < m:
            return self.bs(A, m+1, e)
        else:
            return self.bs(A, b, m-1)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,2,3,4,5],
                5
            ),
            False
        )
    ]
    test(MagicIndex().findMagicIndex, test_data)
