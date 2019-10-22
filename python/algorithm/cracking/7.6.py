# -*- coding:utf-8 -*-

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import defaultdict

class DenseLine:
    def getLine(self, points, n):
        # write code here
        d = defaultdict(int)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d[self.compute(points[i], points[j])] += 1
        m = 0
        rst = None
        for (s, b), c in d.items():
            if c > m:
                rst = [s, b]
                m = c
        return rst

    def compute(self, p1, p2):
        s = 1.0*(p1.y-p2.y)/(p1.x-p2.x)
        b = p1.y - s*p1.x
        return s, b



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 4)],
                4
            ),
            [1, 0]
        )
    ]
    test(DenseLine().getLine, test_data)
