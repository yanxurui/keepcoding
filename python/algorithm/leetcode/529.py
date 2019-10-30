from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.dfs(board, *click)
        return board
    def dfs(self, board, i, j):
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return
        m = self.adjacent(board, i, j)
        if m == 0:
            board[i][j] = 'B'
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x == i and y == j:
                        continue
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and (board[x][y] == 'M' or board[x][y] == 'E'):
                        self.dfs(board, x, y)
        else:
            board[i][j] = str(m)

    def adjacent(self, board, i, j):
        rst = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j:
                    continue
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'M':
                    rst += 1
        return rst



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [
                    ['E', 'E', 'E', 'E', 'E'],
                    ['E', 'E', 'M', 'E', 'E'],
                    ['E', 'E', 'E', 'E', 'E'],
                    ['E', 'E', 'E', 'E', 'E']
                ],
                [3,0]
            ),
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'M', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ]
        ),
        (
            (
                [
                    ['B', '1', 'E', '1', 'B'],
                    ['B', '1', 'M', '1', 'B'],
                    ['B', '1', '1', '1', 'B'],
                    ['B', 'B', 'B', 'B', 'B']
                ],
                [1,2]
            ),
            [
                ['B', '1', 'E', '1', 'B'],
                ['B', '1', 'X', '1', 'B'],
                ['B', '1', '1', '1', 'B'],
                ['B', 'B', 'B', 'B', 'B']
            ]
        ),
    ]
    test(Solution().updateBoard, test_data)

