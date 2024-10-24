from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        ans = 0
        count = 0
        # find all starting points
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        # bfs
        while q:
            i, j = q.popleft()
            for x,y in [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]:
                ans = grid[i][j] - 2
                # found a fresh orange
                if 0 <= x < m and 0 <= y < n and grid[x][y]==1:
                    grid[x][y] = grid[i][j] + 1
                    q.append((x,y))
                    count -= 1

        if count != 0:
            return -1
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[2,1,1],[1,1,0],[0,1,1]],
            4
        ),
        (
            [[2,1,1],[0,1,1],[1,0,1]],
            -1
        ),
        (
            [[0,2]],
            0
        )]
    test(Solution().orangesRotting, test_data)
