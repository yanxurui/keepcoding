from typing import List
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[(i,d)] represents the length of arithmetic sequence that ends at i and has difference d
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                d = A[i]-A[j]
                dp[i, d] = dp.get((j, d), 1) + 1
        return max(dp.values())
 

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [3,6,9,12],
            4
        ),
        (
            [9,4,7,2,10],
            3
        ),
        (
            [20,1,15,3,10,5,8],
            4
        ),
    ]
    test(Solution().longestArithSeqLength, test_data)

