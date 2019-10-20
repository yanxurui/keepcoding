# -*- coding:utf-8 -*-
class CloseNumber:
    def getCloseNumber(self, x):
        print(bin(x))
        # write code here
        # find the first zero bit that has bit 1 on the left 
        s = 1
        i = 0
        while not ((s&x)==0 and ((s<<1) & x)):
            s = s << 1
            i += 1
        # exchange the current
        low = x & (s-1)
        small = ((x | s) ^ (s<<1)) - low + self.max(low, i)

        # find the first one bit that has bit 0 on the left
        b = 1
        while not ((b&x) and ((b<<1) & x)==0):
            b = b << 1
        low = x & (b-1)
        big = ((x ^ b) | (b<<1)) - low + self.min(low)

        return [small, big]

    def count1(self, x):
        rst = 0
        while x:
            x = x&(x-1)
            rst += 1
        return rst

    def max(self, x, n):
        # return the maximum value that keeps the # of 1 bit the same
        m = self.count1(x)
        return ((1<<m)-1)<<(n-m)

    def min(self, x):
        # return the minimum value that keeps the # of 1 bit the same
        m = self.count1(x)
        return (1<<m)-1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            2,
            [1,4]
        ),
        (
            5,
            [3, 6]
        ),
        (
            76351,
            [76284,76383]
        )   
    ]
    test(CloseNumber().getCloseNumber, test_data)
