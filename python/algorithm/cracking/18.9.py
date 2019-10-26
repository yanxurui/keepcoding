# -*- coding:utf-8 -*-
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._before = [] # max heap
        self._after = [] # min heap

    def addNum(self, num):
        if len(self._after) == len(self._before):
            heapq.heappush(self._after, -heapq.heappushpop(self._before, -num))
        else:
            heapq.heappush(self._before, -heapq.heappushpop(self._after, num))

    def findMedian(self):
        if len(self._before) != len(self._after):
            return self._after[0]
        else:
            # return (-self._before[0] + self._after[0]) / 2
            return -self._before[0]

class Middle:
    def getMiddle(self, A, n):
        # write code here
        finder = MedianFinder()
        rst = []
        for i in A:
            finder.addNum(i)
            rst.append(finder.findMedian())
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (
                [1,2,3,4,5,6],6
            ),
            [1,1,2,2,3,3]
        ),
        (
            (
                [6,5,4,3,2,1],6
            ),
            [6,5,5,4,4,3]
        ),
    ]
    test(Middle().getMiddle, test_data)
