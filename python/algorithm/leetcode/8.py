INT_MAX = (1 << 31) - 1
INT_MIN = -(1 << 31)

class Solution:
    def myAtoi(self, str: str) -> int:
        rst = 0
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i >= len(str):
            return rst
        sign = 1
        import pdb
        # pdb.set_trace()
        if str[i] == '-' or str[i] == '+':
            if str[i] == '-':
                sign = -1
            i += 1
        while i < len(str):
            c = str[i]
            if c.isdigit():
                rst = 10 * rst + int(c)
                if rst > INT_MAX:
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                i += 1
            else:
                break
        return sign * rst

        


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            '42',
            42
        ),
        (
            '   -42',
            -42
        ),
        (
            '4193 with words',
            4193
        ),
        (
            'words and 987',
            0
        ),
        (
            '-91283472332',
            -2147483648
        ),
    ]
    test(Solution().myAtoi, test_data)

