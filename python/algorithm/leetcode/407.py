# https://leetcode.com/problems/trapping-rain-water-ii/discuss/89495/How-to-get-the-solution-to-2-D-%22Trapping-Rain-Water%22-problem-from-1-D-case

import heapq

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m = len(heightMap)
        n = 0 if m == 0 else len(heightMap[0])
        heap = []
        visited = [[False for j in range(n)] for i in range(m)]
        rst = 0
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
            visited[i][n-1] = True
        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            visited[0][j] = True
            heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
            visited[m-1][j] = True
        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y]:
                    continue
                visited[x][y] = True
                rst += max(0, h - heightMap[x][y])
                heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [
                  [1,4,3,1,3,2],
                  [3,2,1,3,2,4],
                  [2,3,3,2,3,1]
                ]),
            4
        )
    ]
    test(Solution().trapRainWater, test_data)
