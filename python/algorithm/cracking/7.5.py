# -*- coding:utf-8 -*-
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# 输出为空
class Bipartition:
    def getBipartition(self, A, B):
        # write code here
        x1 = sum(sorted([p[0] for p in A])[1:3])/2.0
        y1 = sum(sorted([p[1] for p in A])[1:3])/2.0
        x2 = sum(sorted([p[0] for p in B])[1:3])/2.0
        y2 = sum(sorted([p[1] for p in B])[1:3])/2.0
        if x1 == x2:
            s = 0
        else:
            s = 1.0*(y2-y1)/(x2-x1)
        b = y1 - s*x1
        return [s, b]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [(0,0),(0,1),(1,1),(1,0)],
                [(1,0),(1,1),(2,0),(2,1)]
            ),
            [0.0, 0.5]
        ),
        (
            (
                [(136,6278),(3958,6278),(3958,2456),(136,2456)],
                [(-3898,11132),(7238,11132),(7238,-4),(-3898,-4)]
            ),
            [-3.17507,10866.36074]
        ),
    ]
    test(Bipartition().getBipartition, test_data,
        compare=lambda l,t: all(abs(a-b) < 1./10000 for a, b in zip(l, t)))
