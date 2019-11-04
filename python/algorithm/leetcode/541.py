class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        buf = []
        for i in range(0, len(s), 2*k):
            buf.append(s[i:i+k][::-1])
            buf.append(s[i+k:i+2*k])
        return ''.join(buf)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'abcdefg',
                2
            ),
            'bacdfeg'
        )
    ]
    test(Solution().reverseStr, test_data)

