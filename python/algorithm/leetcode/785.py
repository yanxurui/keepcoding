from typing import List
from collections import defaultdict

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(int)
        for i in range(len(graph)):
            if color[i] == 0:
                if not self.dfs(graph, i, 1, color):
                    return False
        return True

    def dfs(self, graph, i, c, color):
        color[i] = c
        for j in graph[i]:
            if color[j] == 0:
                if not self.dfs(graph, j, -c, color):
                    return False
            elif color[j] != -c:
                return False
        return True



# BFS
from collections import deque
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(int)
        for i in range(len(graph)):
            if color[i] == 0:
                q = deque([(i, 1)])
                while q:
                    j, c = q.popleft()
                    if color[j] == 0:
                        color[j] = c
                        for k in graph[j]:
                            q.append((k, -c))
                    else:
                        if color[j] != c:
                            return False
        return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[1,3], [0,2], [1,3], [0,2]],
            True
        ),
        (
            [[1,2,3], [0,2], [0,1,3], [0,2]],
            False
        ),
    ]
    test(Solution2().isBipartite, test_data)
