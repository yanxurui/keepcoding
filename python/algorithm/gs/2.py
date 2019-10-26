def gridGame(grid, k, rules):
    # Write your code here
    m = len(grid)
    if m == 0:
        return grid
    n = len(grid[0])
    if n == 0:
        return grid
    for _ in range(k):
        for i in range(m):
            for j in range(n):
                # compute live neighbors
                live = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x == i and y == j:
                            continue
                        if 0 <= x < m and 0 <= y < n:
                            if (grid[x][y] & 1) == 1:
                                live += 1
                if rules[live] == 'alive':
                    grid[i][j] += 2
        for i in range(m):
            for j in range(n):
                grid[i][j] = grid[i][j] >> 1
    return grid



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                ],
                1,
                ['dead', 'alive', 'dead', 'dead', 'dead', 'dead', 'dead', 'dead', 'dead', 'dead']
            ),
            [
                [1, 0, 1, 0],
                [1, 1, 1, 0]
            ]
        ),
        (
            (
                [
                    [0, 1, 0, 0],
                    [0, 0, 0, 0]
                ],
                2,
                ['dead', 'alive', 'dead', 'dead', 'dead', 'alive', 'dead', 'dead', 'dead', 'dead']
            ),
            [
                [0, 1, 0, 0],
                [0, 0, 0, 0]
            ]
        ),
        
    ]
    test(gridGame, test_data)
