# https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations

class Solution:
    '''
    divide two integers without using multiplication, division and mod operator
    '''
    def divide(self, dividend: int, divisor: int) -> int:
        # deal with overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        if (dividend > 0) ^ (divisor > 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            tmp = divisor
            m = 1
            while tmp<<1 < dividend:
                tmp = tmp << 1
                m = m << 1
            dividend -= tmp
            ans += m
        return ans if sign==1 else -ans


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (10, 3),
            3
        ),
        (
            (7, -3),
            -2
        ),
        (
            (-7, 3),
            -2
        ),
        (
            (-7, -3),
            2
        ),
        (
            (1, 1),
            1
        )
    ]
    test(Solution().divide, test_data)
