# -*- coding:utf-8 -*-

class Joseph:
    def getResult(self, n):
        # write code here
        L = range(1, n+1)
        gap = 2
        while len(L) > 1:
            L = L[::gap]
            L.insert(0, L.pop())
            gap += 1
        return L[0]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            5,
            5
        ),
        (
            1,
            1
        ),
        (
            2,
            1
        ),
        (
            3,
            3
        ),
    ]
    test(Joseph().getResult, test_data)
