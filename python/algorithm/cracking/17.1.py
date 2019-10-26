# -*- coding:utf-8 -*-

class Exchange:
    def exchangeAB(self, AB):
        # write code here
        AB[0] ^= AB[1]
        AB[1] ^= AB[0]
        AB[0] ^= AB[1]
        return AB


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1,2],
            [2,1]
        )
    ]
    test(Exchange().exchangeAB, test_data)
