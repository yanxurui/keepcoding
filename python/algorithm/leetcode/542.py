from typing import List
from collections import deque

INT_MAX = (1<<31)-1

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        rst = [[INT_MAX for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    rst[i][j] = 0
                    continue
                if i > 0:
                    # compare with the line above
                    rst[i][j] = min(rst[i-1][j] + 1, rst[i][j])
                if j > 0:
                    # compare with the column on the left
                    rst[i][j] = min(rst[i][j-1] + 1, rst[i][j])
        
        # the second pass in reverse order
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] == 0:
                    rst[i][j] = 0
                    continue
                if i < m-1:
                    rst[i][j] = min(rst[i+1][j] + 1, rst[i][j])
                if j < n - 1:
                    rst[i][j] = min(rst[i][j+1] + 1, rst[i][j])
        return rst

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [[0,0,0],[0,1,0],[0,0,0]],
            [[0,0,0],[0,1,0],[0,0,0]]
        ),
        (
            [[0,0,0],[0,1,0],[1,1,1]],
            [[0,0,0],[0,1,0],[1,2,1]]
        )
    ]
    test(Solution().updateMatrix, test_data)
