class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rise = None
        drop = None
        for i in range(len(nums)):
            if (i == 0 or nums[i] > nums[i-1]) and (i == len(nums)-1 or nums[i] > nums[i+1]):
                return i


# https://leetcode.com/problems/find-peak-element/solutions/1290642/intuition-behind-conditions-complete-explanation-diagram-binary-search/
# binary search
class Solution2(object):
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1
        l = 1
        r = n - 2
        while l <= r:
            m = (l+r)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] < nums[m-1]:
                h = m - 1
            else:
                assert nums[m] < nums[m+1]
                l = m + 1
        return -1

if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ([1,2,3,1]),
            2
        ),
        (
            ([1,2,1,3,5,6,4]),
            5
        ),
        (
            ([1]),
            0
        )
    ]
    test(Solution2().findPeakElement, test_data)
