class Solution:
    def toHex(self, num: int) -> str:
        mapping = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        buf = []
        for i in range(8):
            r = num & 15
            if r < 10:
                buf.append(str(r))
            else:
                buf.append(mapping[r])
            num = num >> 4
            if num == 0:
                break
        return ''.join(buf[::-1])


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            26,
            '1a'
        ),
        (
            -1,
            'ffffffff'
        ),
    ]
    test(Solution().toHex, test_data)

