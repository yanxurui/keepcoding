# https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms

class Solution:
    def solveNQueens(self, n):
        def DFS(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                results.append(queens)
                return
            for q in range(n):
                if not (q in queens or p-q in xy_diff or p+q in xy_sum):
                    # xy_diff: 135 diagonal
                    # xy_sum: 45 diagonal
                    DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
        results = []
        DFS([], [], [])
        return [['.'*q+'Q'+'.'*(n-q-1) for q in sol] for sol in results]


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            4,
            [
                [
                ".Q..",
                "...Q",
                "Q...",
                "..Q."
                ],
                [
                "..Q.",
                "Q...",
                "...Q",
                ".Q.."
                ]
            ]
        )
    ]
    test(Solution().solveNQueens, test_data)

