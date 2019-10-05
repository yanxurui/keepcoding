# https://leetcode.com/problems/power-of-two/discuss/63966/4-different-ways-to-solve-Iterative-Recursive-Bit-operation-Math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1) == 0)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (1),
            True
        ),
        (
            (16),
            True
        ),
        (
            (218),
            False
        )
    ]
    test(Solution().isPowerOfTwo, test_data)
