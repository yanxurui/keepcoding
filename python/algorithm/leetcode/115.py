class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        table = [[0 for j in range(len(t)+1)] for i in range(len(s)+1)]
        for i in range(len(s)+1):
            table[i][0] = 1
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    table[i+1][j+1] = table[i][j] + table[i][j+1]
                else:
                    table[i+1][j+1] = table[i][j+1]
        return table[len(s)][len(t)]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                "rabbbit",
                "rabbit"
            ),
            3
        ),
        (
            (
                "baabb",
                "ab"
            ),
            4
        ),
        (
            (
                "babgbag",
                "bag"
            ),
            5
        )
    ]
    test(Solution().numDistinct, test_data)

