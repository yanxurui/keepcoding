# https://leetcode.com/problems/race-car/discuss/124326/Summary-of-the-BFS-and-DP-solutions-with-intuitive-explanation
import sys

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [sys.maxsize] * (target + 1)
        dp[0] = 0
        for i in range(1, target+1):
            j = 0
            m = 0
            while j < i:
                p = 0
                q = 0
                while p < j:
                    dp[i] = min(dp[i], dp[j]+1+q+1+dp[i-(j-p)])
                    q += 1
                    p = (1<<q) - 1
                m += 1
                j = (1<<m) - 1
            if i == j:
                dp[i] = min(dp[i], m)
            else:
                assert i < j
                dp[i] = min(dp[i], m+1+dp[j-i])
        return dp[target]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (3),
            2
        ),
        (
            (6),
            5
        )
    ]
    test(Solution().racecar, test_data)
