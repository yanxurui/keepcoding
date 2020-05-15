class Solution(object):
    def recursive(self, s1, s2, s3, l1, l2, l3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if l3 == 0:
            return True
        yes = self.table.get((l1, l2, l3), None)
        if yes is not None:
            return yes
        if (l1 > 0 and s3[l3-1] == s1[l1-1] and self.recursive(s1, s2, s3, l1-1, l2, l3-1)) or \
           (l2 > 0 and s3[l3-1] == s2[l2-1] and self.recursive(s1, s2, s3, l1, l2-1, l3-1)):
            yes = True
        else:
            yes = False
        self.table[(l1, l2, l3)] = yes
        return yes

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        self.table = dict()
        return self.recursive(s1, s2, s3, len(s1), len(s2), len(s3))


# https://leetcode.com/problems/interleaving-string/discuss/31879/My-DP-solution-in-C%2B%2B
class Solution2(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        # dp[i][j] is True represents s1[:i] and s2[:j] can wave to s3[:i+j]
        # i, j means the length of s1 and s2 respectively
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    if s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                        dp[i][j] = True
                elif j == 0:
                    if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                        dp[i][j] = True
                else:
                    if s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                        dp[i][j] = True
                    elif s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                        dp[i][j] = True
        return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                "aabcc",
                "dbbca",
                "aadbbcbcac"
            ),
            True
        ),
        (
            
            (
                "aabcc",
                "dbbca",
                "aadbbbaccc"
            ),
            False
        ),
        (
            
            (
                "a",
                "",
                "c"
            ),
            False
        ),
        (
            
            (
                "db",
                "b",
                "cbb",
            ),
            False
        ),
    ]
    test(Solution2().isInterleave, test_data)

