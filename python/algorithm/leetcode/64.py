class Solution(object):
    def dhs(self, grid, x, y):
        if x == 0 or y == 0:
            return self.table[(x,y)]

        m = self.table.get((x,y), None)
        if m is None:
            m = grid[x][y] + min(self.dhs(grid, x-1, y), self.dhs(grid, x, y-1))
            self.table[(x,y)] = m
        return m

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        self.table = dict()
        self.table[(0,0)] = grid[0][0]
        for i in range(1,m):
            self.table[(i,0)] = self.table[(i-1,0)] + grid[i][0]
        for j in range(1,n):
            self.table[(0,j)] = self.table[(0,j-1)] + grid[0][j]
        import pdb
        # pdb.set_trace()
        return self.dhs(grid, m-1, n-1)

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [
                [1,3,1],
                [1,5,1],
                [4,2,1]
            ],
            7
        )
    ]
    test(Solution().minPathSum, test_data)
