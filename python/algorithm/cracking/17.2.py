# -*- coding:utf-8 -*-

class Board:
    def checkWon(self, board):
        # write code here
        if board[0][0] + board[1][1] +board[2][2] == 3:
            return True
        if board[0][2] + board[1][1] +board[2][0] == 3:
            return True
        for i in range(3):
            if board[i][0] + board[i][1] + board[i][2] == 3:
                return True
            if board[0][i] + board[1][i] + board[2][i] == 3:
                return True
        return False


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [
                [1, 0, 1],
                [1,-1,-1],
                [1,-1, 0]
            ],
            True
        )
    ]
    test(Board().checkWon, test_data)
