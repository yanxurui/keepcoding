# -*- coding:utf-8 -*-
class GoUpstairs:
    def countWays(self, n):
        # write code here
        a = [0] * 4
        a[0] = 1
        for i in range(1, n+1):
            k = i % 4
            a[k] = (a[k-1] + a[k-2] + a[k-3])%1000000007
        return a[k]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            1,
            1
        ),
        (
            3,
            4
        ),
        (
            4,
            7
        ),
        (
            100000,
            111787461
        )
    ]
    test(GoUpstairs().countWays, test_data)
