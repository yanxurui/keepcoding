# -*- coding:utf-8 -*-
class Transform:
    def calcCost(self, A, B):
        # write code here
        return self.count1(A^B)

    def count1(self, x):
        rst = 0
        while x:
            x = x&(x-1)
            rst += 1
        return rst

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (10,5),
            4
        ) 
    ]
    test(Transform().calcCost, test_data)
