# https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/Python-concise-solution-with-dictionary.

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:
                return True
            else:
                d[n] = i
        return False


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                [1,2,3,1],
                3
            ),
            True
        ),
        (
            (
                [1,0,1,1],
                1
            ),
            True
        ),
        (
            (
                [1,2,3,1,2,3],
                2
            ),
            False
        ),
        
    ]
    test(Solution().containsNearbyDuplicate, test_data)
