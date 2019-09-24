class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rise = None
        drop = None
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                rise = True
                drop = False
            else:
                if rise:
                    return i - 1
                else:
                    rise = False
                    drop = True
            if i == len(nums) - 1:
                if rise:
                    return i


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            ([1,2,3,1]),
            2
        ),
        (
            ([1,2,1,3,5,6,4]),
            1
        ),
        (
            ([1]),
            0
        )
    ]
    test(Solution().findPeakElement, test_data)
