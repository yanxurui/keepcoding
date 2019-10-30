from typing import List
from collections import Counter
import heapq

class Item:
    def __init__(self, w, c):
        self.w = w
        self.c = c
    def __lt__(self, o):
        if self.c == o.c:
            return self.w > o.w
        return self.c < o.c

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for w, c in count.items():
            ele = Item(w, c)
            if len(heap) < k:
                heapq.heappush(heap, ele)
            elif heap[0] < ele:
                heapq.heapreplace(heap, ele)
        rst = []
        l = len(heap)
        for i in range(l):
            rst.append(heapq.heappop(heap).w)
        return rst[::-1]

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                ["i", "love", "leetcode", "i", "love", "coding"],
                2
            ),
            ["i", "love"]
        ),
        (
            (
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4
            ),
            ["the", "is", "sunny", "day"]
        )
    ]
    test(Solution().topKFrequent, test_data)
