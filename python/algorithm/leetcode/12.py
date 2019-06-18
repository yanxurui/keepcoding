class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        assert num >=1 and num <= 3999

        ans = []
        n = num // 1000
        ans.append('M'*n)
        num %= 1000

        n = num//100
        if n == 9:
            ans.append('CM')
        elif n > 5:
            ans.append('D'+'C'*(n-5))
        elif n == 5:
            ans.append('D')
        elif n == 4:
            ans.append('CD')
        else:
            ans.append('C'*n)
        num %= 100

        n = num//10
        if n == 9:
            ans.append('XC')
        elif n > 5:
            ans.append('L'+'X'*(n-5))
        elif n == 5:
            ans.append('L')
        elif n == 4:
            ans.append('XL')
        else:
            ans.append('X'*n)
        num %= 10

        n = num
        if n == 9:
            ans.append('IX')
        elif n > 5:
            ans.append('V'+'I'*(n-5))
        elif n == 5:
            ans.append('V')
        elif n == 4:
            ans.append('IV')
        else:
            ans.append('I'*n)
        return ''.join(ans)

    
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            3,
            "III"
        ),
        (
            4,
            "IV"
        ),
        (
            9,
            "IX"
        ),
        (
            58,
            "LVIII"
        ),
        (
            1994,
            "MCMXCIV"
        )
    ]
    test(Solution().intToRoman, test_data)

