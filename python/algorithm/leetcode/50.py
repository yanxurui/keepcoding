# https://leetcode.com/problems/powx-n/discuss/?currentPage=1&orderBy=most_votes&query=

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            n = -n
            x = 1/x

        return self.myPow(x*x, n//2) if n%2==0 else x*self.myPow(x*x, n//2)

if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (2.00000, 10),
            1024.00000
        ),
        (
            (2.10000, 3),
            9.26100
        ),
        (
            (2.00000, -2),
            0.25000
        )
    ]
    test(Solution().myPow, test_data)

