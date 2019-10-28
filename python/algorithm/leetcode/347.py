from typing import List
from collections import Counter
import heapq

class Node:
    def __init__(self, v, f):
        self.v = v
        self.f = f
    def __lt__(self, o):
        return self.f >= o.f

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [Node(v, f) for v,f in count.items()]
        heapq.heapify(heap)
        rst = []
        for i in range(k):
            rst.append(heapq.heappop(heap).v)
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,1,1,2,2,3],
                2
            ),
            [1,2]
        ),
        (
            (
                [1],
                1
            ),
            [1]
        ),
    ]
    test(Solution().topKFrequent, test_data)

