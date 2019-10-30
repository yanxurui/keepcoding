# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution

import sys
import heapq
from typing import List
from collections import defaultdict, deque
INT_MAX = sys.maxsize

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        edges = defaultdict(list)
        for u, v, w in flights:
            edges[u].append((v, w))
        q = [(0, src, K+1)]
        while q:
            price, city, steps = heapq.heappop(q)
            if city == dst:
                return price
            if steps > 0:
                for nxt, w in edges[city]:
                    heapq.heappush(q, (price+w, nxt, steps-1))
        return -1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                3,
                [[0,1,100],[1,2,100],[0,2,500]],
                0, 2, 1
            ),
            200
        ),
        (
            (
                3,
                [[0,1,100],[1,2,100],[0,2,500]],
                0, 2, 0
            ),
            500
        ),
        (
            (
                4,
                [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                0, 3, 1
            ),
            6
        ),
    ]
    test(Solution().findCheapestPrice, test_data)

