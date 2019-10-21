class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]


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
    ]
    test(Solution().isPalindrome, test_data)

