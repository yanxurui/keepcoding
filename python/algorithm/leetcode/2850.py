# https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/solutions/4028356/python-3-6-lines-permutation-w-explanation-t-s-88-ms-16-mb/

from typing import List

INT_MAX = (1 << 31) - 1

class Solution:
    def permutations(self, nums):
        '''
        there are many duplicates
        '''
        ans = [[]]
        for n in nums:
            new_ans = []
            for an in ans:
                for i in range(len(an)+1):
                    new_ans.append(an[:i] + [n] + an[i:])
                    if i < len(an) and an[i] == n:
                        break
            ans = new_ans
        return ans

    def minimumMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dist = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1])
        zeros = []
        spares = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zeros.append((i, j))
                elif grid[i][j] > 1:
                    spares.extend([(i,j)] * (grid[i][j]-1))
        assert len(zeros) == len(spares)
        ans = INT_MAX
        for spares_p in self.permutations(spares):
            s = sum(map(dist, zeros, spares_p))
            if s < ans:
                ans = s
        return ans


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [[1,1,0],[1,1,1],[1,2,1]],
            3
        ),
        (
            [[1,3,0],[1,0,0],[1,0,3]],
            4
        )
    ]
    test(Solution().minimumMoves, test_data)
