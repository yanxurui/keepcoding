class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n//3)
        else:
            return False

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            27,
            True
        ),
        (
            0,
            False
        ),
        (
            1,
            True
        ),
        (
            45,
            False
        ),
    ]
    test(Solution().isPowerOfThree, test_data)
