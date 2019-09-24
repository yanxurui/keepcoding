# https://leetcode.com/problems/maximum-gap/discuss/50643/bucket-sort-JAVA-solution-with-explanation-O(N)-time-and-space

import sys

INT_MAX = sys.maxsize  

INT_MIN = -sys.maxsize-1

from math import ceil


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        min_v, max_v = min(nums), max(nums)
        gap = ceil((max_v - min_v) / (n - 1))
        min_bucket = [INT_MAX] * (n - 1)
        max_bucket = [INT_MIN] * (n - 1)
        for i in nums:
            if i == max_v or i == min_v:
                continue
            idx = (i - min_v) // gap
            min_bucket[idx] = min(min_bucket[idx], i)
            max_bucket[idx] = max(max_bucket[idx], i)
        max_gap = 0
        prev = min_v
        for i in range(n-1):
            if min_bucket[i] == INT_MAX and max_bucket[i] == INT_MIN:
                continue # empty bucket
            max_gap = max(max_gap, min_bucket[i] - prev)
            prev = max_bucket[i]
        max_gap = max(max_gap, max_v - prev)
        return max_gap


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ([3,6,9,1]),
            3
        ),
        (
            ([10]),
            0
        ),
        (
            ([15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]),
            2901
        )
    ]
    test(Solution().maximumGap, test_data)
