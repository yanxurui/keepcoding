# -*- coding:utf-8 -*-

class Factor:
    def getFactorSuffixZero(self, n):
        # write code here
        rst = 0
        i = 5
        while i <= n:
            rst += (n//i)
            i *= 5
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            5,
            1
        ),
        (
            25,
            6
        ),
    ]
    test(Factor().getFactorSuffixZero, test_data)
