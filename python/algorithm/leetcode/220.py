# https://leetcode.com/problems/contains-duplicate-iii/discuss/61645/AC-O(N)-solution-in-Java-using-buckets-with-explanation

import sys
INT_MIN = -sys.maxsize-1

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        buckets = {}
        for i, n in enumerate(nums):
            key = (n - INT_MIN) // (t+1)
            if key in buckets or (key+1) in buckets and buckets[key+1] - n <= t \
            or (key-1) in buckets and n - buckets[key-1] <= t:
                return True
            buckets[key] = n
            if len(buckets) > k:
               del buckets[(nums[i-k] - INT_MIN) // (t+1)]
        return False


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                [1,2,3,1],
                3,
                0
            ),
            True
        ),
        (
            (
                [1,0,1,1],
                1,
                2
            ),
            True
        ),
        (
            (
                [1,5,9,1,5,9],
                2,
                3
            ),
            False
        ),
        
    ]
    test(Solution().containsNearbyAlmostDuplicate, test_data)
