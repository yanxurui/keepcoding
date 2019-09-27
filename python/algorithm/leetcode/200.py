class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    input1 = '''11110
11010
11000
00000'''
    input2 = '''11000
11000
00100
00011'''

    test_data = [
        (
            ([list(l) for l in input1.split()]),
            1
        ),
        (
            ([list(l) for l in input2.split()]),
            3
        ),
    ]
    test(Solution().numIslands, test_data)
