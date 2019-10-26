# -*- coding:utf-8 -*-

INT_MIN = -(1<<31)

class MaxSum:
    def getMaxSum(self, A, n):
        # write code here
        dp = [INT_MIN]
        for i in range(n):
            dp.append(max(dp[-1], 0)+A[i])
        return max(dp)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,2,3,-6,1],
                5
            ),
            6
        ),
        (
            (
                [-1],
                1
            ),
            -1
        ),
    ]
    test(MaxSum().getMaxSum, test_data)
