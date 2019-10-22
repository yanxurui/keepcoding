# -*- coding:utf-8 -*-
class CrossLine:
    def checkCrossLine(self, s1, s2, y1, y2):
        # write code here
        return not (s1 == s2 and y1 != y2)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (3.14,3.14,1,2),
            False
        )
    ]
    test(CrossLine().checkCrossLine, test_data)
