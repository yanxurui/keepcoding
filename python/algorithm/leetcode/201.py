# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56746/One-line-C%2B%2B-solution

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.rangeBitwiseAnd(m//2, n//2)<<1 if m < n else m


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (5, 7),
            4
        ),
        (
            (0, 1),
            0
        ),
    ]
    test(Solution().rangeBitwiseAnd, test_data)
