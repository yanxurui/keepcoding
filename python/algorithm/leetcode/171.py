class Solution:
    def titleToNumber(self, s: str) -> int:
        ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = 0
        for c in s:
            res = res * 26 + ALPHA.index(c) + 1
        return res

if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ('A'),
            1
        ),
        (
            ("AB"),
            28
        ),
        (
            ("ZY"),
            701
        ),
        (
            ("AZ"),
            52
        )
    ]
    test(Solution().titleToNumber, test_data)
