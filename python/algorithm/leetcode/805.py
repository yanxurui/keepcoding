# https://leetcode.com/problems/split-array-with-same-average/discuss/120667/C%2B%2B-Solution-with-explanation-early-termination-(Updated-for-new-test-case)
from typing import List

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        s = sum(A)
        l = len(A)
        m = len(A)//2
        possible = False
        for k in range(1, m+1):
            if s * k % l == 0:
                possible = True
        if not possible:
            return False
        # dp[k] means possible sum of k elements from A
        dp = [set() for k in range(m+1)]
        dp[0].add(0)
        for i, n in enumerate(A):
            for k in range(min(m, i+1), 0, -1):
                # in reverse order to prevent overwritting
                for p in dp[k-1]:
                    dp[k].add(p+n)
        for k in range(1, m+1):
            if s*k%l == 0 and s*k//l in dp[k]:
                return True
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,2,3,4,5,6,7,8],
            True
        ),
        (
            [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5],
            True
        ),
    ]
    test(Solution().splitArraySameAverage, test_data)

