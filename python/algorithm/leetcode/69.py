# https://leetcode.com/problems/sqrtx/discuss/25047/A-Binary-Search-Solution/24042

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            4,
            2
        ),
        (
            8,
            2
        ),
        (
            2147395599,
            46339
        )
    ]
    test(Solution().mySqrt, test_data)
