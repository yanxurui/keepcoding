class Solution(object):
    def search(self, nums, low, high, target):
        if low > high:
            return [-1,-1]
        mid = (low+high)/2
        m = nums[mid]
        if m==target:
            s = mid
            e = mid
            while s >=0 and nums[s] == target:
                s -= 1
            while e < len(nums) and nums[e] == target:
                e += 1
            return [s+1, e-1]
        elif m > target:
            return self.search(nums, low, mid-1, target)
        else:
            return self.search(nums, mid+1, high, target)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.search(nums, 0, len(nums)-1, target)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([5,7,7,8,8,10], 8),
            [3, 4]
        ),
        (
            ([5,7,7,8,8,10], 6),
            [-1, -1]
        ),
        (
            ([1,2,2,2,3], 2),
            [1,3]
        ),
        (
            ([1,2],2),
            [1,1]
        )
    ]
    test(Solution().searchRange, test_data)
