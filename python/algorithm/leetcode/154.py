# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48808/My-pretty-simple-code-to-solve-it

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        while l < h:
            m = l + (h - l)//2
            if nums[m] < nums[h]:
                h = m
            elif nums[m] > nums[h]:
                l = m + 1
            else:
                h -= 1
        return nums[l]

        
if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ([3,4,5,1,2] ),
            1
        ),
        (
            ([4,5,6,7,0,1,2]),
            0
        ),
        (
            ([1,3,5]),
            1
        ),
        (
            ([2,2,2,0,1]),
            0
        ),
        (
            ([3,1,3]),
            1
        )
    ]
    test(Solution().findMin, test_data)

