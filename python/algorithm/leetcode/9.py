class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]

class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x%10 == 0):
            return False
        # e.g.,
        # x = 12321
        # x = 12321, y = 0
        # x = 1232, y = 1
        # x = 123, y = 12
        # x = 12, y = 123
        y = 0
        while x > y:
            y = 10 * y + (x % 10)
            x = x // 10
        if x == y or x == (y // 10):
            # even or odd
            return True
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            121,
            True
        ),
        (
            -121,
            False
        ),
        (
            10,
            False
        ),
        (
            0,
            True
        )
    ]
    test(Solution2().isPalindrome, test_data)

