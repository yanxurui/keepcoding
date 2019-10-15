# https://leetcode.com/problems/game-of-life/discuss/73223/Easiest-JAVA-solution-with-explanation
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return board
        for i in range(len(board)):
            for j in range(len(board[0])):
                n = self.lives(board, i, j)
                if (board[i][j] & 1) and (n == 2 or n == 3):
                    board[i][j] = 3 # 01 -> 11
                elif (board[i][j] & 1)==0 and n == 3:
                    board[i][j] = 2 # 00 -> 10
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] >> 1

    def lives(self, board, x, y):
        rst = 0
        for i in range(max(0,x-1), min(len(board),x+2)):
            for j in range(max(0,y-1), min(len(board[0]),y+2)):
                if i == x and j == y:
                    continue
                if (board[i][j] & 1) == 1:
                    rst += 1
        return rst


def wrapper(board):
    Solution().gameOfLife(board)
    return board


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
              [0,1,0],
              [0,0,1],
              [1,1,1],
              [0,0,0]
            ],
            [
              [0,0,0],
              [1,0,1],
              [0,1,1],
              [0,1,0]
            ]
        )
    ]
    test(wrapper, test_data)

