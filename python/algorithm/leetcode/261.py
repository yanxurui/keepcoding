from typing import List

class UnionFind:
    def __init__(self, nums):
        self.d = {}
        for n in nums:
            self.d[n] = n

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a == b:
            return False
        else:
            self.d[a] = b
            return True

    def find(self, x):
        while self.d[x] != x:
            x = self.d[x]
        return x

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        uf = UnionFind(range(n))
        for x, y in edges:
            if not uf.union(x, y):
                # there is a circle
                return False
        return True


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                5,
                [[0,1],[0,2],[0,3],[1,4]]
            ),
            True
        ),
        (
            (
                5,
                [[0,1],[1,2],[2,3],[1,3],[1,4]]
            ),
            False
        )
    ]

    test(Solution().validTree, test_data)
