from typing import List

class UnionFind:
    def __init__(self, nums):
        self._parent = {}
        self.size = len(nums)
        for n in nums:
            self._parent[n] = n

    def find(self, x):
        if x == self._parent[x]:
            return x
        else:
            return self.find(self._parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self._parent[px] = py
        if px != py:
            self.size -= 1

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        uf = UnionFind(range(N))
        for i in range(N):
            for j in range(i):
                if M[i][j] == 1:
                    uf.union(i, j)
        return uf.size


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                [1,1,0],
                [1,1,0],
                [0,0,1]
            ],
            2
        ),
        (
            [
                [1,1,0],
                [1,1,1],
                [0,1,1]
            ],
            1
        ),
    ]
    test(Solution().findCircleNum, test_data)

