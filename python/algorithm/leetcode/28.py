class Solution:
    def build(self, needle):
        idx = [-1] * len(needle)
        for i in range(1, len(needle)):
            k = idx[i-1]
            while k >= 0 and needle[k+1] != needle[i]:
                k = idx[k]
            if needle[k+1] == needle[i]:
                idx[i] = k+1
        return idx

    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        idx = self.build(needle)
        k = 0
        for i, c in enumerate(haystack):
            while k != 0 and not needle[k] == c:
                k = idx[k-1] + 1
            if needle[k] == c:
                k += 1
                if k == len(needle):
                    return i - k + 1

        return -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                'hello',
                'll'
            ),
            2
        ),
        (
            (
                'aaaaa',
                'bba'
            ),
            -1
        ),
        (
            (
                'aaaaa',
                ''
            ),
            0
        ),
        
    ]
    test(Solution().strStr, test_data)
