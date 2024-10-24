import math
from typing import List
from collections import deque

# BFS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        efforts = [[math.inf for i in range(n)] for j in range(m)]
        efforts[0][0] = 0
        dq = deque([(0,0)])
        while dq:
            i, j = dq.popleft()
            for x, y in [(i-1, j),(i,j-1),(i+1,j),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    newEffort = max(efforts[i][j], abs(heights[i][j]-heights[x][y]))
                    if newEffort < efforts[x][y]:
                        # (x,y) is updated, we need to update all neighbors of it as well
                        efforts[x][y] = newEffort
                        dq.append((x,y))
        return efforts[m-1][n-1]


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            [[1,2,2],[3,8,2],[5,3,5]],
            2
        ),
        (
            [[1,2,3],[3,8,4],[5,3,5]],
            1
        ),
        (
            [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
            0
        ),
        (
            [[1,10,6,7,9,10,4,9]],
            9
        )
    ]
    test(Solution().minimumEffortPath, test_data)

