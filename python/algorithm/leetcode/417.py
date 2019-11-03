from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        pacific = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            self.dfs(matrix, pacific, i, 0)
        for j in range(n):
            self.dfs(matrix, pacific, 0, j)

        atlantic = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            self.dfs(matrix, atlantic, i, n-1)
        for j in range(n):
            self.dfs(matrix, atlantic, m-1, j)
        return self.intersect(pacific, atlantic)

    def dfs(self, matrix, ocean, i, j):
        ocean[i][j] = True
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                if not ocean[x][y] and matrix[x][y] >= matrix[i][j]:
                    self.dfs(matrix, ocean, x, y)
    def intersect(self, ocean1, ocean2):
        rst = []
        for i in range(len(ocean1)):
            for j in range(len(ocean1[0])):
                if ocean1[i][j] and ocean2[i][j]:
                    rst.append([i, j])
        return rst



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                [1,  2,  2,  3,  5,],
                [3,  2,  3,  4,  4,],
                [2,  4,  5,  3,  1,],
                [6,  7,  1,  4,  5,],
                [5,  1,  1,  2,  4,],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        )
    ]
    test(Solution().pacificAtlantic, test_data)

