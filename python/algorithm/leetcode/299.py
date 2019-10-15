from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        cow = bull = 0
        for c1,c2 in zip(secret, guess):
            if c1 == c2:
                cow += 1
            else:
                d1[c1] += 1
                d2[c2] += 1
        for k,v in d2.items():
            bull += min(d1[k], v)
        return '{}A{}B'.format(cow, bull)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                '1807',
                '7810'
            ),
            '1A3B'
        ),
        (
            (
                '1123',
                '0111'
            ),
            '1A1B'
        )
    ]
    test(Solution().getHint, test_data)

