from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if len(board) == 0 or len(board[0]) == 0:
            return 0
        cnt = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if (i-1 < 0 or board[i-1][j] == '.') and (j-1 < 0 or board[i][j-1] == '.'):
                        cnt += 1
        return cnt


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                ['X','.','.','X'],
                ['.','.','.','X'],
                ['.','.','.','X']
            ],
            2
        )
    ]
    test(Solution().countBattleships, test_data)

