class Solution(object):
    def __init__(self):
        self.table = {
            1:1,
            2:2
        }
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        r = self.table.get(n, None)
        if r is not None:
            return r
        else:
            r = self.climbStairs(n-1) + self.climbStairs(n-2)
            self.table[n] = r
            return r
        
class Solution2(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            2,
            2
        ),
        (
            3,
            3
        ),
        (
            35,
            14930352
        )
    ]
    test(Solution2().climbStairs, test_data)
