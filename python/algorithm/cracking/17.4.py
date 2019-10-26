# -*- coding:utf-8 -*-

class Max:
    def getMax(self, a, b):
        # write code here
        c = (a-b)>>31 # 0 if a>=b else -1
        return a+c*(a-b)

    def getMax2(self, a, b):
        # write code here
        return (a+b+abs(a-b))//2

    def getMax3(self, a, b):
        # write code here
        b = a-b
        return a+(b>>31)*b
    


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (1, 2),
            2
        )
    ]
    test(Max().getMax, test_data)
