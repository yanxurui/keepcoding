# https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)

from collections import defaultdict

class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        d = defaultdict(set)
        for e in edges:
            d[e[0]].add(e[1])
            d[e[1]].add(e[0])
        rst = [0] * N
        cnt = [1] * N # cnt[i] means the # of sub-nodes of node i
        def pre_dfs(root, prev):
            # only rst[0] will be the final value
            for n in d[root]:
                if n != prev:
                    pre_dfs(n, root)
                    cnt[root] += cnt[n]
                    rst[root] += rst[n] + cnt[n]
        def post_dfs(root, prev):
            for n in d[root]:
                if n != prev:
                    # move root to n
                    rst[n] = rst[root] - cnt[n] + N - cnt[n]
                    post_dfs(n, root)
        pre_dfs(0, -1)
        post_dfs(0, -1)
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
