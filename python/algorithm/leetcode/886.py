from typing import List
from collections import defaultdict

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for i, j in dislikes:
            edges[i].append(j)
            edges[j].append(i)

        colors = defaultdict(int)
        for i in range(1, N+1):
            if colors[i] == 0:
                if not self.dfs(edges, i, 1, colors):
                    return False
        return True

    def dfs(self, edges, i, c, colors):
        if colors[i] == 0:
            colors[i] = c
            for j in edges[i]:
                if not self.dfs(edges, j, -c, colors):
                    return False
        else:
            if colors[i] != c:
                return False
        return True



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                4,
                [[1,2],[1,3],[2,4]]
            ),
            True
        ),
        (
            (
                3,
                [[1,2],[1,3],[2,3]]
            ),
            False
        ),
        (
            (
                5,
                [[1,2],[2,3],[3,4],[4,5],[1,5]]
            ),
            False
        ),
    ]
    test(Solution().possibleBipartition, test_data)
