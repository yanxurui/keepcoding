# DP
# time complexity: N^2xKx8
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[1 for j in range(N)] for i in range(N)]
        for k in range(K):
            new_dp = [[0 for j in range(N)] for i in range(N)]
            for x in range(N):
                for y in range(N):
                    for i, j in [(x-2,y+1),(x-1,y+2),(x+1,y+2),(x+2,y+1),(x+2,y-1),(x+1,y-2),(x-1,y-2),(x-2,y-1)]:
                        if 0<=i<N and 0<=j<N:
                            new_dp[x][y] += 1/8 * dp[i][j]
            dp = new_dp
        return dp[r][c]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (3, 2, 0, 0),
            0.0625
        )
    ]
    test(Solution().knightProbability, test_data)

