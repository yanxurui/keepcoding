class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        a, b = 0, 1
        for i in range(2, N+1):
            a, b = b, a+b
        return b


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            2,
            1
        ),
        (
            3,
            2
        ),
        (
            4,
            3
        ),
        (
            0,
            0
        ),
    ]
    test(Solution().fib, test_data)

