# https://leetcode.com/problems/dungeon-game/discuss/52774/C%2B%2B-DP-solution

import sys

INT_MAX = sys.maxsize  

class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        tab = [[INT_MAX for j in range(N+1)] for i in range(M+1)]
        tab[M][N-1] = 1
        tab[M-1][N] = 1
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                # how many points are needed for position (i,j)? x
                # we need to satisfy dungeon[i][j] + x >= min(tab[i+1][j], tab[i][j+1])
                # x >= min(tab[i+1][j], tab[i][j+1]) - dungeon[i][j] + x
                need = min(tab[i+1][j], tab[i][j+1]) - dungeon[i][j]
                if need <= 0:
                    need = 1
                # tab[i][j] represents the minimum points needed to
                # find a way from position (i,j) to the bottom right corner
                tab[i][j] = need
        return tab[0][0]


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                [
                    [-2,-3,3],
                    [-5,-10,1],
                    [10,30,-5]
                ]
            ),
            7
        ),
        (
            (
                [[-1,1]]
            ),
            2
        )
    ]
    test(Solution().calculateMinimumHP, test_data)
