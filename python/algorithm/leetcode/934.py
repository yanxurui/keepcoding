from typing import List
class Solution:
    def paintOneIsland(self, grid):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if self.dfs(grid, i, j):
                    return

    def dfs(self, grid, i, j):
        if min(i, j) >= 0 and max(i, j) < len(grid):
            if grid[i][j] == 1:
                grid[i][j] = 2
                self.dfs(grid, i-1, j)
                self.dfs(grid, i+1, j)
                self.dfs(grid, i, j-1)
                self.dfs(grid, i, j+1)
                return True
        return False

    def expand(self, grid, x, y):
        '''
        return True if reaches island 1
        '''
        l = grid[x][y]
        for i, j in ((x-1,y), (x+1, y), (x, y-1), (x, y+1)):
            if min(i, j) >= 0 and max(i, j) < len(grid):
                if grid[i][j] == 1:
                    return True
                elif grid[i][j] == 0:
                    grid[i][j] = l + 1
        return False


    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.paintOneIsland(grid)
        n = len(grid)
        for l in range(2, 2*n):
            # find l and expand one
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == l and self.expand(grid, i, j):
                        return l-2


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [[0,1],[1,0]],
            1
        ),
        (
            [[0,1,0],[0,0,0],[0,0,1]],
            2
        ),
        (
            [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]],
            1
        )
    ]
    test(Solution().shortestBridge, test_data)
