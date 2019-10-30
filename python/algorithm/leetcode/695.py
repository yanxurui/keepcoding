from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rst = 0
        q = deque()
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # find a new island
                    # bfs
                    q.append((i, j))
                    tmp = 0
                    while q:
                        x, y = q.popleft()
                        if grid[x][y] == 1:
                            tmp += 1
                            grid[x][y] = 0
                            for x2,y2 in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                                    q.append((x2, y2))
                    if tmp > rst:
                        rst = tmp
        return rst


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rst = 0
        stack = []
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # find a new island
                    # dfs
                    stack.append((i, j))
                    tmp = 0
                    while stack:
                        x, y = stack.pop()
                        if grid[x][y] == 1:
                            tmp += 1
                            grid[x][y] = 0
                            for x2,y2 in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                                if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                                    stack.append((x2, y2))
                    if tmp > rst:
                        rst = tmp
        return rst



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                [0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]
            ],
            6  
        ),
        (
            [[0,0,0,0,0,0,0,0]],
            0
        ),
        (
            [
                [1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,0,1,1],
                [0,0,0,1,1]
            ],
            4
        ),
    ]
    test(Solution2().maxAreaOfIsland, test_data)

