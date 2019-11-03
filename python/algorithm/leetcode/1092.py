# https://leetcode.com/problems/shortest-common-supersequence/discuss/312710/C%2B%2BPython-Find-the-LCS

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.LCS(str1, str2)
        i = j = 0
        rst = []
        for c in lcs:
            while str1[i] != c:
                rst.append(str1[i])
                i += 1
            while str2[j] != c:
                rst.append(str2[j])
                j += 1
            rst.append(c)
            i += 1
            j += 1
        rst.append(str1[i:])
        rst.append(str2[j:])
        return ''.join(rst)

    def LCS(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [['' for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + text1[i-1]
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1], key=len)
        return dp[m][n]



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'abac',
                'cab'
            ),
            'cabac'
        )
    ]
    test(Solution().shortestCommonSupersequence, test_data)

