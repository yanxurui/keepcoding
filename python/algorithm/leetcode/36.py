from collections import defaultdict

class Solution(object):
    def valid(self, digits):
        digits.pop('.', None)
        for v in digits.values():
            if v != 1:
                return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        digits = defaultdict(int)

        for r in range(9):
            digits.clear()
            for c in range(9):
                digits[board[r][c]] += 1
            if not self.valid(digits):
                return False

        for c in range(9):
            digits.clear()
            for r in range(9):
                digits[board[r][c]] += 1
            if not self.valid(digits):
                return False

        for r in range(0,9,3):
            for c in range(0,9,3):
                digits.clear()
                for rs in range(3):
                    for cs in range(3):
                        digits[board[r+rs][c+cs]] += 1
                if not self.valid(digits):
                    return False
        return True

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [
              ["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ],
            True
        ),
        (
            [
              ["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]
            ],
            False
        )
    ]
    test(Solution().isValidSudoku, test_data)
