from typing import List
from collections import defaultdict

class Solution:
    def comb2(self, n):
        return n*(n-1)//2

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = defaultdict(int)
        for n in time:
            count[n%60] += 1
        rst = 0
        for i in range(1, 30):
            rst += (count[i]*count[60-i])
        rst += self.comb2(count[0])
        rst += self.comb2(count[30])
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [30,20,150,100,40],
            3
        ),
        (
            [60,60,60],
            3
        ),
    ]
    test(Solution().numPairsDivisibleBy60, test_data)

