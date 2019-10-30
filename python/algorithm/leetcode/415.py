class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        r = 0
        i = len(num1)-1
        j = len(num2)-1
        buf = []
        while i >= 0 or j >=0:
            if i >= 0:
                r += int(num1[i])
                i -= 1
            if j >= 0:
                r += int(num2[j])
                j -= 1
            buf.append(r%10)
            r //= 10
        if r:
            buf.append(r)
        return ''.join(map(str, buf[::-1]))


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                '1',
                '2'
            ),
            '3'
        ),
        (
            (
                '10',
                '2'
            ),
            '12'
        ),
        (
            (
                '9',
                '1'
            ),
            '10'
        ),
        (
            (
                '0',
                '1'
            ),
            '1'
        ),
        (
            (
                '0',
                '0'
            ),
            '0'
        ),
        (
            (
                '1000000000000000',
                '9000000000000000'
            ),
            '10000000000000000'
        ),
    ]
    test(Solution().addStrings, test_data)

