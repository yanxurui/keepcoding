# https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        table = [0] * (len(s)+1)
        table[0] = 1
        table[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s)+1):
            if int(s[i-1:i]) >= 1 and int(s[i-1:i]) <= 9:
                table[i] += table[i-1]
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                table[i] += table[i-2]
        return table[len(s)]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            "12",
            2
        ),
        (
            "226",
            3
        ),
        (
            '0',
            0
        ),
        (
            '10',
            1
        ),
        (
            '00',
            0
        ),
        (
            '01',
            0
        )
    ]
    test(Solution().numDecodings, test_data)
