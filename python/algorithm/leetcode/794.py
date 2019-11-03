from typing import List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        count_of_O = self.count(board, 'O')
        count_of_X = self.count(board, 'X')

        win_of_O = self.win(board, 'O')
        win_of_X = self.win(board, 'X')
        
        if win_of_X > 1 or win_of_O > 1:
            return False
        elif win_of_X and win_of_O:
            return False
        elif win_of_X:
            return count_of_X - count_of_O == 1
        elif win_of_O:
            return count_of_X == count_of_O
        else:
            return count_of_X - count_of_O == 1 or count_of_X == count_of_O

    def count(self, board, x):
        rst = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == x:
                    rst += 1
        return rst
    def win(self, board, x):
        rst = 0
        X = x*3
        row = 0
        for i in range(3):
            if board[i] == X:
                row += 1
        col = 0
        for i in range(3):
            if board[0][i]+board[1][i]+board[2][i] == X:
                col += 1
        diag = 0
        if board[0][0]+board[1][1]+board[2][2] == X or board[0][2]+board[1][1]+board[2][0] == X:
            diag += 1
        return max(row, col, diag)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ["O  ", "   ", "   "],
            False
        ),
        (
            ["XOX", " X ", "   "],
            False
        ),
        (
            ["XXX", "   ", "OOO"],
            False
        ),
        (
            ["XOX", "O O", "XOX"],
            True
        ),
        (
            ["XOX", "OXO", "XOX"],
            True
        ),
        (
            ["XXX","XOO","OO "],
            False
        ),
        (
            ["XXX","XOO","OO "],
            False
        ),
    ]
    test(Solution().validTicTacToe, test_data)

