# https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python

from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        cnt = defaultdict(int)
        rst = 0
        for a in A:
            for b in B:
                cnt[a+b] += 1
        for c in C:
            for d in D:
                rst += cnt[0-c-d]
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [ 1, 2],
                [-2,-1],
                [-1, 2],
                [ 0, 2]
            ),
            2
        )
    ]
    test(Solution().fourSumCount, test_data)
