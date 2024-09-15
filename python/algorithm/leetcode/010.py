# https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        # initialize
        dp[0][0] = True
        for j in range(len(p)):
            if j >= 1 and p[j] == '*' and dp[0][j-1]:
                dp[0][j+1] = True
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if j >= 1:
                        if p[j-1] == s[i] or p[j-1] == '.':
                            # a* or .* match >1, 1, 0 chars
                            dp[i+1][j+1] = dp[i][j+1] or \
                                           dp[i][j-1] or \
                                           dp[i+1][j-1]
                        else:
                            # a* or .* match empty
                            dp[i+1][j+1] = dp[i+1][j-1]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'aa',
                'a'
            ),
            False
        ),
        (
            (
                'aa',
                'a*'
            ),
            True
        ),
        (
            (
                'ab',
                '.*'
            ),
            True
        ),
        (
            (
                'aab',
                'c*a*b'
            ),
            True
        ),
        (
            (
                'mississippi',
                'mis*is*p*.'
            ),
            False
        ),
        (
            (
                'aaaab',
                'a*ab'
            ),
            True
        ),
        (
            (
                "aaa",
                "a*a"
            ),
            True
        ),
        (
            (
                "aaa",
                "ab*a*c*a"
            ),
            True
        ),
        (
            (
                "a",
                "c*a"
            ),
            True
        ),
    ]
    test(Solution().isMatch, test_data)

