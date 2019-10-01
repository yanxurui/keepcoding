class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ([1,2,3,1]),
            True
        ),
        (
            ([1,2,3,4]),
            False
        ),
        (
            ([1,1,1,3,3,4,3,2,4,2]),
            True
        )
    ]
    test(Solution().containsDuplicate, test_data)
