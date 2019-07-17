import operator
from functools import reduce

class Solution(object):
    def c(self, n,k):
        if k == 0:
            return 1
        if n == k:
            return 1
        return reduce(operator.mul, range(n-k+1, n+1))/reduce(operator.mul, range(1, k+1))

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for k in range(rowIndex//2+1):
            res.append(self.c(rowIndex, k))
        for k in range(rowIndex//2+1,rowIndex+1):
            res.append(res[rowIndex-k])
        return res

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            3,
            [1,3,3,1]
        ),
    ]
    test(Solution().getRow, test_data)
