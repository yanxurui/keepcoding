# https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts

from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adjs = [set() for i in range(n)]
        for i, j in edges:
            adjs[i].add(j)
            adjs[j].add(i)
        leaves = [i for i in range(n) if len(adjs[i])==1]
        while n > 2:
            # remove leaves
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adjs[i].pop()
                adjs[j].remove(i)
                if len(adjs[j]) == 1:
                    newLeaves.append(j)
            leaves = newLeaves
        return leaves


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                4,
                [[1, 0], [1, 2], [1, 3]]
            ),
            [1]
        ),
        (
            (
                6,
                [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
            ),
            [3, 4]
        ),
        (
            (
                1,
                []
            ),
            [0]
        )
    ]
    test(Solution().findMinHeightTrees, test_data)
