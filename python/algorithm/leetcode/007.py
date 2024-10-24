INT_MAX = (1 << 31) -1
INT_MIN = -(INT_MAX+1)

class Solution:
    def reverse(self, x: int) -> int:
        buf = []
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        while x:
            buf.append(x % 10)
            x //= 10
        rst = 0
        for i in buf:
            rst = 10 * rst + i
        rst *= sign
        if rst > INT_MAX or rst < INT_MIN:
            return 0
        else:
            return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            123,
            321
        ),
        (
            -123,
            -321
        ),
        (
            120,
            21
        )
    ]
    test(Solution().reverse, test_data)

