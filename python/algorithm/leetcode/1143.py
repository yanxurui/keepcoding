class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[m][n]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'abcde',
                'ace'
            ),
            3
        ),
        (
            (
                'abc',
                'abc'
            ),
            3
        ),
        (
            (
                'abc',
                'def'
            ),
            0
        ),
    ]
    test(Solution().longestCommonSubsequence, test_data)

