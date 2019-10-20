# -*- coding:utf-8 -*-
class Exchange:
    def exchangeOddEven(self, x):
        # write code here
        odd = (x & int('10'*16, base=2)) >> 1
        even = (x & int('01'*16, base=2)) << 1
        return odd | even


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            10,
            5
        )
    ]
    test(Exchange().exchangeOddEven, test_data)
