from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque([])
        for i in range(len(num)):
            while k > 0 and q and q[-1] > num[i]:
                q.pop()
                k -= 1
            q.append(num[i])
        # for corner case 111
        while k > 0:
            q.pop()
            k -= 1
        while q and q[0] == '0':
            q.popleft()
        if q:
            return ''.join(q)
        else:
            return '0'


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                '1432219',
                3
            ),
            '1219'
        ),
        (
            (
                '10200',
                1
            ),
            '200'
        ),
        (
            (
                '10',
                2
            ),
            '0'
        ),
        (
            (
                '111',
                2
            ),
            '1'
        ),
        (
            (
                '111',
                3
            ),
            '0'
        ),
        (
            (
                "1234567890",
                9
            ),
            '0'
        ),
    ]
    test(Solution().removeKdigits, test_data)

