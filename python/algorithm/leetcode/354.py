# https://leetcode.com/problems/russian-doll-envelopes/discuss/82763/Java-NLogN-Solution-with-Explanation
from typing import List
from functools import cmp_to_key

def my_cmp(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        if a[1] > b[1]:
            return -1
        elif a[1] < b[1]:
            return 1
        else:
            return 0
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes = sorted(envelopes, key=cmp_to_key(my_cmp))
        # solve longest increasing sub-sequence
        dp = []
        for w, h in envelopes:
            i = self.bs(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

    def bs(self, nums, t):
        # find the first one that is > target
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if t <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l






if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[5,4],[6,4],[6,7],[2,3]],
            3
        )
    ]
    test(Solution().maxEnvelopes, test_data)

