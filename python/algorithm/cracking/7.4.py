# -*- coding:utf-8 -*-
class AddSubstitution:
    def calc(self, a, b, t):
        # write code here
        if t == 1:
            return self.multiply(a, b)
        elif t == 0:
            return self.divide(a, b)
        elif t == -1:
            return self.subtract(a, b)

    def multiply(self, a, b):
        if a < b:
            return self.multiply(b, a)
        rst = 0
        for i in range(b):
            rst += a
        return rst

    def subtract(self, a, b):
        if b > a:
            return -self.subtract(b, a)
        rst = 0
        while rst + b < a:
            rst += 1
        return rst
    
    def divide(self, a, b):
        rst = 0
        s = 0
        while s + b <= a:
            s += b
            rst += 1
        return rst





if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (1,2,1),
            2
        )
    ]
    test(AddSubstitution().calc, test_data)
