class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1 or N == 2:
            return N
        if N == 3 or N == 4:
            return N + 3
        r = N % 4
        if r == 0:
            return N + 1
        if r == 1 or r == 2:
            return N + 2
        if r == 3:
            return N-1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            4,
            7
        ),
        (
            10,
            12
        ),
    ]
    test(Solution().clumsy, test_data)

