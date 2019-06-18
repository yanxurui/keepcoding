class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = []
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == 'M':
                ans.append(1000)
            elif c == 'D':
                ans.append(500)
            elif c == 'C':
                if i+1<n and (s[i+1]=='M' or s[i+1]=='D'):
                    ans.append(-100)
                else:
                    ans.append(100)
            elif c == 'L':
                ans.append(50)
            elif c == 'X':
                if i+1<n and (s[i+1]=='C' or s[i+1]=='L'):
                    ans.append(-10)
                else:
                    ans.append(10)
            elif c == 'V':
                ans.append(5)
            elif c == 'I':
                if i+1<n and (s[i+1]=='X' or s[i+1]=='V'):
                    ans.append(-1)
                else:
                    ans.append(1)
            else:
                raise Exception('wrong input')
        return sum(ans)

    
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            "III",
            3
        ),
        (
            "IV",
            4
        ),
        (
            "IX",
            9
        ),
        (
            "LVIII",
            58
        ),
        (
            "MCMXCIV",
            1994
        )
    ]
    test(Solution().romanToInt, test_data)

