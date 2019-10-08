# https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return []
        xor = 0
        for n in nums:
            xor = xor ^ n
        mask = 1
        while not (mask & xor):
            mask = mask << 1
        a = b = 0
        for n in nums:
            if mask & n:
                a ^= n
            else:
                b ^= n
        return [a, b]


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ([1,2,1,3,2,5]),
            [3, 5]
        )
    ]
    test(Solution().singleNumber, test_data, compare=unordered_equal)
