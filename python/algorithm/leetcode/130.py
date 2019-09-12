class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    self.dfs(board, i, j, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'Y':
                    board[i][j] = 'O'

    def dfs(self, board, i, j, m, n):
        if i >=0 and i < m and j >=0 and j < n:
            if board[i][j] == 'O':
                board[i][j] = 'Y'
                self.dfs(board, i-1, j, m, n) # up
                self.dfs(board, i+1, j, m, n) # down
                self.dfs(board, i, j-1, m, n) # left
                self.dfs(board, i, j+1, m, n) # right



def wrapper(board):
    Solution().solve(board)
    return board
        

if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            ([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]),
            [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        ),
        (
            ([["O","O","O"],["O","O","O"],["O","O","O"]]),
            [["O","O","O"],["O","O","O"],["O","O","O"]]
        )
    ]
    test(wrapper, test_data)
