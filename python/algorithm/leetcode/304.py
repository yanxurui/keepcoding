from copy import copy
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        self._matrix = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):        
                self._matrix[i+1][j+1] = matrix[i][j] + self._matrix[i][j+1] + self._matrix[i+1][j] - self._matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._matrix[row2+1][col2+1] - self._matrix[row2+1][col1] - self._matrix[row1][col2+1] + self._matrix[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (2, 1, 4, 3),
            8
        ),
        (
            (1, 1, 2, 2),
            11
        ),
        (
            (1, 2, 2, 4),
            12
        )
    ]
    matrix = [
              [3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]
            ]
    obj = NumMatrix(matrix)
    test(obj.sumRegion, test_data)
