class Solution:
    def isUgly(self, num: int) -> bool:
        if not num > 0:
            return False
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        return num == 1
            

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            1,
            True
        ),
        (
            6,
            True
        ),
        (
            8,
            True
        ),
        (
            14,
            False
        ),
        (
            0,
            False
        )
    ]
    test(Solution().isUgly, test_data)
