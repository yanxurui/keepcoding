# https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)
# DP
# TLE because python is slow

import sys
INT_MAX = sys.maxsize

class Solution:
    def numSquares(self, n: int) -> int:
        # tab[i] is the least number of perfect squares that sum to i
        tab = [INT_MAX] * (n+1)
        tab[0] = 0
        for i in range(1, n+1):
            j = 1
            while j**2 <= i:
                # i must be the sum of a smaller num i-j*j and a perfect square j*j
                tab[i] = min(tab[i], tab[i-j**2]+1)
                j += 1
        return tab[n]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            12,
            3
        ),
        (
            13,
            2
        ),
        (
            6730,
            2
        ),
    ]
    test(Solution().numSquares, test_data)
