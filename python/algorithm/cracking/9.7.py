# -*- coding:utf-8 -*-

from collections import deque

class Flood:
    def floodFill(self, tmap, n, m):
        m, n = n, m
        # write code here
        visited = [[0 for j in range(n)] for i in range(m)]
        visited[0][0] = 1
        level = deque([(0, 0)])
        rst = 0
        while True:
            l = len(level)
            for i in range(l):
                x, y = level.popleft()
                if x == m-1 and y == n-1:
                    return rst
                else:
                    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if 0 <= i < m and 0 <= j < n and not visited[i][j] and tmap[i][j] != 1:
                            level.append((i, j))
                            visited[i][j] = 1
            rst += 1        


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [
                    [0,1,0,0,0],
                    [0,0,0,1,0],
                    [0,0,1,0,0],
                    [0,1,0,0,0],
                ],
                4, 5
            ),
            9
        )
    ]
    test(Flood().floodFill, test_data)
