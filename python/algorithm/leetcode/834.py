import sys
from collections import defaultdict

INT_MAX = sys.maxsize

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = defaultdict(lambda: defaultdict(lambda: INT_MAX))
        nodes = set()
        for e in edges:
            d[e[0]][e[1]] = 1
            d[e[1]][e[0]] = 1
            nodes.add(e[0])
            nodes.add(e[1])
        for n, others in d.items():
            for o1 in others:
                for o2 in others:
                    if o1 != o2:
                        d[o1][o2] = d[o2][o1] = min(d[o1][o2], d[n][o1]+d[n][o2])
        rst = []
        for i in range(N):
            rst.append(sum(d[i].values()))
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (
                6,
                [[0,1],[0,2],[2,3],[2,4],[2,5]],
            ),
            [8, 12, 6, 10, 10, 10]
        )
    ]
    test(Solution().sumOfDistancesInTree, test_data)
