import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # n bulbs: 1,2,...,n
        # in the i-th round, bulbs whose # can be divisble by i will be toggled
        # if 1<=m<=n can be divisible by i<=m, then there must exist j<=m that i*j=m
        # if i!=j, bulb m will be left off
        # if i==j, bulb m will be toggled on
        # find bulbs whose # is squared of a smaller number
        return int(math.sqrt(n))


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            3,
            1
        ),
        (
            0,
            0
        ),
        
    ]
    test(Solution().bulbSwitch, test_data)
