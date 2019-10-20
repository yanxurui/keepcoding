# -*- coding:utf-8 -*-
import math
def isclose(a, b):
    return abs(a-b) < 1e-06
class BinDecimal:
    def printBin(self, num):
        # write code here
        tmp = self.decimal(num-int(num))
        if len(tmp) > 32:
            return 'Error'
        else:
            return '0.'+tmp

    def interger(self, num):
        rst = []
        if num == 0:
            return '0'
        while num:
            rst.append(num%2)
            num //= 2
        return ''.join(map(str, rst[::-1]))
    def decimal(self, num):
        N = 33
        rst = []
        for i in range(N):
            if isclose(num, 0):
                break
            num *= 2
            rst.append(int(num))
            num = num - int(num)
        return ''.join(map(str, rst))


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            0.625,
            '0.101'
        ),
        (
            0.11111111111,
            'Error'
        ),
        (
            0.03125,
            '0.00001'
        ),
        
    ]
    test(BinDecimal().printBin, test_data)
