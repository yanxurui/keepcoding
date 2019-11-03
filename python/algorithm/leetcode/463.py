from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if 0<=x<len(grid) and 0<=y<len(grid[0]):
                            if grid[x][y] == 0:
                                count += 1
                        else:
                            count += 1
        return count


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[0,1,0,0],
             [1,1,1,0],
             [0,1,0,0],
             [1,1,0,0]],
            16
        ),
        (
            [[1]],
            4
        ),
    ]
    test(Solution().islandPerimeter, test_data)

