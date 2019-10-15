# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version < 4:
        return False
    else:
        return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        return self.bs(1, n)

    def bs(self, l, r):
        # assume 4 is the first bad version
        # 2,3 -> m=2,l=4
        # 3,4 -> m=3,l=4
        # 4,5 -> m=4,l=4
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            5,
            4
        ),
    ]
    test(Solution().firstBadVersion, test_data)
