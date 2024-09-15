# https://leetcode.com/problems/min-cost-to-connect-all-points/solutions/843995/python-3-min-spanning-tree-prim-s-algorithm/
# Prim's algo
import heapq
from typing import List
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        manhattan = lambda p1, p2: abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        cost = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                cost[i].append((d, j))
                cost[j].append((d, i))
        ans = 0
        count = 1
        visited = [False] * n
        visited[0] = True
        q = cost[0]
        heapq.heapify(q)
        while count < n:
            d, i = heapq.heappop(q)
            if not visited[i]:
                ans += d
                count += 1
                visited[i] = True
                for e in cost[i]:
                    heapq.heappush(q, e)
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[0,0],[2,2],[3,10],[5,2],[7,0]],
            20
        ),
        (
            [[3,12],[-2,5],[-4,1]],
            18
        ),
    ]
    test(Solution().minCostConnectPoints, test_data)
