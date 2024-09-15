class Solution(object):
    def recursive(self, mask, board, word, k, x, y):
        if k == len(word):
            return True
        m = len(board)
        n = len(board[0])
        if x >= 0 and x < m and y >= 0 and y < n:
            if mask[x][y] == 0 and board[x][y] == word[k]:
                mask[x][y] = 1
                found = self.recursive(mask, board, word, k+1, x-1, y) \
                    or self.recursive(mask, board, word, k+1, x+1, y) \
                    or self.recursive(mask, board, word, k+1, x, y-1) \
                    or self.recursive(mask, board, word, k+1, x, y+1)
                mask[x][y] = 0
                return found
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        mask = [[0 for j in row] for row in board]
        for i in range(m):
            for j in range(n):
                if self.recursive(mask, board, word, 0, i, j):
                    return True
        return False

        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [
                    ['A','B','C','E'],
                    ['S','F','C','S'],
                    ['A','D','E','E']
                ],
                "ABCCED"
            ),
            True
        ),
        (
            (
                [
                    ['A','B','C','E'],
                    ['S','F','C','S'],
                    ['A','D','E','E']
                ],
                "SEE"
            ),
            True
        ),
        (
            (
                [
                    ['A','B','C','E'],
                    ['S','F','C','S'],
                    ['A','D','E','E']
                ],
                "ABCB"
            ),
            False
        ),
    ]
    test(Solution().exist, test_data)
