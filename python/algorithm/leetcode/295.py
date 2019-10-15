# https://zhuanlan.zhihu.com/p/85283794
from typing import List
import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._before = [] # max heap
        self._after = [] # min heap

    def addNum(self, num: int) -> None:
        if len(self._after) == len(self._before):
            heapq.heappush(self._after, -heapq.heappushpop(self._before, -num))
        else:
            heapq.heappush(self._before, -heapq.heappushpop(self._after, num))

    def findMedian(self) -> float:
        if len(self._before) != len(self._after):
            return self._after[0]
        else:
            return (-self._before[0] + self._after[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    assert obj.findMedian() == 1
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2

    obj = MedianFinder()
    obj.addNum(-1)
    obj.addNum(-2)
    assert obj.findMedian() == -1.5
    obj.addNum(-3)
    import pdb
    # pdb.set_trace()
    assert obj.findMedian() == -2


# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]