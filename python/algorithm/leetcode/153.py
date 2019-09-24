class Solution(object):
    def bin_search(self, nums):
        l = len(nums)
        if l == 1 or nums[0] < nums[-1]:
            return nums[0]
        else:
            return min(self.bin_search(nums[:l//2]), self.bin_search(nums[l//2:]))
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.bin_search(nums)

        
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
        )
    ]
    test(Solution().findMin, test_data)

