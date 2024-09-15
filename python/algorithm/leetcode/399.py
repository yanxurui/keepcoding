from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, graph, b, e, val, visited):
        if b in visited:
            return -1
        if b == e:
            # found
            return val
        visited[b] = True
        for n, v in graph[b]:
            # from b to n
            ans = self.dfs(graph, n, e, val*v, visited)
            if ans != -1:
                return ans
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, e in enumerate(equations):
            u = e[0]
            v = e[1]
            graph[u].append((v, values[i]))
            graph[v].append((u, 1/values[i]))
        ans = []
        for q in queries:
            u = q[0]
            v = q[1]
            visited = {}
            if u in graph and v in graph:
                ans.append(self.dfs(graph, u, v, 1, visited))
            else:
                ans.append(-1)
        return ans

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [["a","b"],["b","c"]],
                [2.0,3.0],
                [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
            ),
            [6.00000,0.50000,-1.00000,1.00000,-1.00000]
        ),
        (
            (
                [["a","b"],["b","c"],["bc","cd"]],
                [1.5,2.5,5.0],
                [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
            ),
            [3.75000,0.40000,5.00000,0.20000]
        ),
        (
            (
                [["a","b"]],
                [0.5],
                [["a","b"],["b","a"],["a","c"],["x","y"]]
            ),
            [0.50000,2.00000,-1.00000,-1.00000]
        ),
        
    ]
    test(Solution().calcEquation, test_data)

