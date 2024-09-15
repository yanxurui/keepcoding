from typing import List
from collections import defaultdict, deque

# DFS recursive
class Solution:
    def dfs(self, graph, s, d, visited, path):
        if s == d:
            return True
        if s in visited:
            return False
        path.append(s)
        visited[s] = True
        for k in graph[s]:
            if self.dfs(graph, k, d, visited, path):
                return True
        path.pop()
        return False

    def validgraph(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = defaultdict(bool)
        path = [] # stack
        return self.dfs(graph, source, destination, visited, path)


# DFS iterative
class Solution2:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = defaultdict(bool)
        st = [source] # stack
        while st:
            k = st.pop()
            if k == destination:
                return True
            for i in graph[k]:
                if i not in visited:
                    st.append(i)
                    visited[k] = True
        return False

# BFS iterative
class Solution3:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = defaultdict(bool)
        q = deque([source]) # queue
        while q:
            k = q.popleft()
            if k == destination:
                return True
            for i in graph[k]:
                if i not in visited:
                    q.append(i)
                    visited[k] = True
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                3,
                [[0,1],[1,2],[2,0]],
                0,
                2
            ),
            True
        ),
        (
            (
                6,
                [[0,1],[0,2],[3,5],[5,4],[4,3]],
                0,
                5
            ),
            False
        )
    ]
    test(Solution3().validPath, test_data)

