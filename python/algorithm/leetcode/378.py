from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heap = [(matrix[0][0], 0,0)]
        seen = set((0,0))
        for i in range(k):
            v, i, j = heapq.heappop(heap)
            for x, y in [(i+1, j), (i, j+1)]:
                if x < m and y < n and (x,y) not in seen:
                    seen.add((x,y))
                    heapq.heappush(heap, (matrix[x][y], x, y))
        return v

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85173/Share-my-thoughts-and-Clean-Java-Code
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        heap = [(matrix[0][j], 0,j) for j in range(n)] # first row
        for i in range(k):
            v, i, j = heapq.heappop(heap)
            if i+1 < m:
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
        return v


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [
                   [ 1,  5,  9],
                   [10, 11, 13],
                   [12, 13, 15]
                ],
                8
            ),
            13
        )
    ]
    test(Solution2().kthSmallest, test_data)

