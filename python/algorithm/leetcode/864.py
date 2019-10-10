class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        m = len(grid)
        n = 0 if m == 0 else len(grid[0])
        moves = set()
        keys = '.@abcdef' # chars that can be stepped on
        num_keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_i = i
                    start_j = j
                elif grid[i][j] in 'abcdef':
                    num_keys += 1
        queue = [[start_i, start_j, 0, keys, 0]] # x, y, steps, key string, collected keys
        while queue:
            i, j, steps, keys, collected_keys = queue.pop(0)
            if grid[i][j] in 'abcdef' and  grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collected_keys += 1
                if collected_keys == num_keys:
                    return steps
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0<=x<m and 0<=y<n and grid[x][y] in keys:
                    move = (x, y, keys)
                    if move not in moves:
                        moves.add(move)
                        queue.append([x, y, steps+1, keys, collected_keys])
        return -1

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ["@.a.#","###.#","b.A.B"],
            8
        ),
        (
            ["@..aA","..B#.","....b"],
            6
        ),
    ]
    test(Solution().shortestPathAllKeys, test_data)

