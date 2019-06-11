from collections import defaultdict
from pprint import pprint
from copy import deepcopy

def loc(i, j):
    return i//3*3+j/3

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        All = set(map(str,list(range(1,10))))
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        subs = [set() for i in range(9)]
        for i,r in enumerate(board):
            for j,c in enumerate(r):
                if c != '.':
                    rows[i].add(c)
                    cols[j].add(c)
                    subs[loc(i,j)].add(c)
        seq = []
        for i,r in enumerate(board):
            for j,c in enumerate(r):
                if c == '.':
                    possible = All.difference(rows[i].union(cols[j]).union(subs[loc(i,j)]))
                    seq.append((i,j,possible))
        seq = sorted(seq, key=lambda v: len(v[2]))
        seq_bak = deepcopy(seq)
        stack = defaultdict(list)
        k = 0
        while k >= 0 and k < len(seq):
            i,j,possible = seq[k]
            # print(k,(i,j))
            # print(possible)
            if stack[k]:
                c = stack[k][-1]
                rows[i].remove(c)
                cols[j].remove(c)
                subs[loc(i,j)].remove(c)
            c = None # necessary
            while len(possible)>0:
                c = possible.pop()

                if not (c in rows[i] or c in cols[j] or c in subs[loc(i,j)]):
                    break
                c = None
            if not c:
                assert len(possible) == 0
                # print('backtrack')
                # have tried all possible values
                # revert: how?
                # try a different value at last position
                seq[k] = deepcopy(seq_bak[k])
                stack[k] = []
                k -= 1

            else:
                # print(c)
                stack[k].append(c)
                rows[i].add(c)
                cols[j].add(c)
                subs[loc(i,j)].add(c)
                k += 1

        for k,(i,j,_) in enumerate(seq):
            board[i][j] = stack[k][-1]




def wrapper(board):
    Solution().solveSudoku(board)
    return board

        
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
            [
              ["5","3","4","6","7","8","9","1","2"],
              ["6","7","2","1","9","5","3","4","8"],
              ["1","9","8","3","4","2","5","6","7"],
              ["8","5","9","7","6","1","4","2","3"],
              ["4","2","6","8","5","3","7","9","1"],
              ["7","1","3","9","2","4","8","5","6"],
              ["9","6","1","5","3","7","2","8","4"],
              ["2","8","7","4","1","9","6","3","5"],
              ["3","4","5","2","8","6","1","7","9"]
            ]
        )
    ]
    test(wrapper, test_data)
