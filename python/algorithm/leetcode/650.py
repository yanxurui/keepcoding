class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = i
            for j in range(i-1, 1, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i//j)
        return dp[n]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            3,
            3
        ),
        (
            7,
            7
        ),
        (
            12,
            7
        ),

    ]
    test(Solution().minSteps, test_data)

