class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        else:
            return max(self.robUtil(nums[0:len(nums)-1]), self.robUtil(nums[1:len(nums)]))

    def robUtil(self, nums):
        n = len(nums)
        max_previous = nums[0]
        max_current = max(nums[0], nums[1])
        for i in range(2, n):
            tmp = max(max_current, max_previous+nums[i])
            max_previous = max_current
            max_current = tmp
        return max_current


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            (
                [2,3,2],
            ),
            3
        ),
        (
            (
                [1,2,3,1]
            ),
            4
        )
    ]
    test(Solution().rob, test_data)
