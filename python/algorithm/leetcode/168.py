class Solution:
    def convertToTitle(self, n: int) -> str:
        ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        buf = []
        while n:
            r = n % 26
            buf.append(ALPHA[r-1])
            n = n // 26
            if r == 0:
                n -= 1
        return ''.join(buf[::-1])


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (1),
            'A'
        ),
        (
            (28),
            'AB'
        ),
        (
            (701),
            "ZY"
        ),
        (
            (52),
            "AZ"
        ),
        (
            26**2,
            "YZ"
        ),
    ]
    test(Solution().convertToTitle, test_data)
