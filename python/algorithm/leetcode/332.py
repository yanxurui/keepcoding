from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        N = len(tickets)
        for t in tickets:
            edges[t[0]].append(t[1])
        for k, v in edges.items():
            v.sort()
        d = 'JFK'
        return self.backtrack(edges, d, N)

    def backtrack(self, edges, d, N):
        rst = [d]
        for i, a in enumerate(edges[d]):
            edges[d].pop(i)
            tmp = self.backtrack(edges, a, N-1)
            if len(tmp) == N:
                return rst + tmp
            edges[d].insert(i, a)
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"]
        ),
        (
            [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
            ["JFK","ATL","JFK","SFO","ATL","SFO"]
        ),
        (
            [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
            ["JFK","NRT","JFK","KUL"]
        ),
        (
            [
                ["EZE","AXA"],
                ["TIA","ANU"],
                ["ANU","JFK"],
                ["JFK","ANU"],
                ["ANU","EZE"],
                ["TIA","ANU"],
                ["AXA","TIA"],
                ["TIA","JFK"],
                ["ANU","TIA"],
                ["JFK","TIA"]
            ],
            ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
        )
    ]
    test(Solution().findItinerary, test_data)
