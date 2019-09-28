class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.loop(n, set())

    def loop(self, n, seen):
        if n == 1:
            return True
        seen.add(n)        
        s = 0
        while n:
            s += (n%10)**2
            n = n//10
        if s in seen:
            return False
        return self.loop(s, seen)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (19),
            True
        ),
        (
            (1),
            True
        ),
        (
            (2),
            False
        ),
    ]
    test(Solution().isHappy, test_data)
