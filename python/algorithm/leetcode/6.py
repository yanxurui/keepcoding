class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rst = [[] for i in range(numRows)]
        k = 2 * numRows - 2
        for i, c in enumerate(s):
            r = i % k
            if r < numRows:
                rst[r].append(c)
            else:
                rst[k - r].append(c)
        return ''.join([''.join(row) for row in rst])


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'PAYPALISHIRING',
                3
            ),
            'PAHNAPLSIIGYIR'
        ),
        (
            (
                'PAYPALISHIRING',
                4
            ),
            'PINALSIGYAHRPI'
        ),
    ]
    test(Solution().convert, test_data)

