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
    test(Solution().climbStairs, test_data)
