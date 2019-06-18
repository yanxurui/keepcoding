class Solution:
    def totalNQueens(self, n: int) -> int:
        def DFS(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                return 1
            ans = 0
            for q in range(n):
                if not (q in queens or p-q in xy_diff or p+q in xy_sum):
                    # xy_diff: 135 diagonal
                    # xy_sum: 45 diagonal
                    ans += DFS(queens+[q], xy_diff+[p-q], xy_sum+[p+q])
            return ans
        ans = DFS([], [], [])
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            4,
            2
        )
    ]
    test(Solution().totalNQueens, test_data)
