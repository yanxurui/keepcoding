# -*- coding:utf-8 -*-

import sys

INT_MAX = sys.maxsize

class Distance:
    def getDistance(self, article, n, x, y):
        # write code here
        i1, i2 = None, None
        rst = INT_MAX
        for i, w in enumerate(article):
            if w == x:
                i1 = i
                if i2:
                    rst = min(rst, i1-i2)
            elif w == y:
                i2 = i
                if i1:
                    rst = min(rst, i2-i1)
        return rst



if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                ['a', 'b', 'a', 'c', 'd', 'b'],
                6,
                'a', 'd'
            ),
            2
        ),
    ]
    test(Distance().getDistance, test_data)
