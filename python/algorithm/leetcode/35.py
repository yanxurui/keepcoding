class Solution(object):
    def search(self, nums, l, h, t):
        if l > h:
            if l == -1:
                return 0
            else:
                return l
        mid = (l+h)/2
        m = nums[mid]
        if m == t:
            return mid
        elif m < t:
            return self.search(nums, mid+1, h, t)
        else:
            return self.search(nums, l, mid-1, t)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search(nums, 0, len(nums)-1, target)

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([1,3,5,6], 5),
            2
        ),
        (
            ([1,3,5,6], 2),
            1
        ),
        (
            ([1,3,5,6], 7),
            4
        ),
        (
            ([1,3,5,6], 0),
            0
        ),
        (
            ([1,3],2),
            1
        )
    ]
    test(Solution().searchInsert, test_data)
