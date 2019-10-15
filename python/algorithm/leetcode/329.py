# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78308/15ms-Concise-Java-Solution
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = 0
        cache = {}
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m, self.dfs(matrix, i, j, cache))
       
        return m

    def dfs(self, matrix, i, j, cache):
        m = cache.get((i,j), None)
        if m:
            return m
        m = 0
        for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[i][j] >= matrix[x][y]:
                continue
            m = max(m, self.dfs(matrix, x, y, cache))
        m += 1
        cache[(i,j)] = m
        return m


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                [
                  [9,9,4],
                  [6,6,8],
                  [2,1,1]
                ] 
            ),
            4
        ),
        (
            [
              [3,4,5],
              [3,2,6],
              [2,2,1]
            ],
            4
        )
    ]
    test(Solution().longestIncreasingPath, test_data)
