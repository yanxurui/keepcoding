class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        dp[n] = 0 # at least 2
        for i in range(1, n+1):
            for j in range(1, i):
                if j > i-j:
                    break
                dp[i] = max(dp[i], dp[j]*dp[i-j])
        return dp[n]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            2,
            1
        ),
        (
            10,
            36
        ),
    ]
    test(Solution().integerBreak, test_data)

