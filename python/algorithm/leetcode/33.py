class Solution(object):
    def sub_search(self, nums, low, high, target):
        med = (low + high)/2
        m = nums[med]
        if m == target:
            return med
        if med == low:
            if nums[high] == target:
                return high
            else:
                return -1
        if m > nums[low]:
            if m < target:
                return self.sub_search(nums, med, high, target)
            else:
                if nums[low] > target:
                    return self.sub_search(nums, med, high, target)
                else:
                    return self.sub_search(nums, low, med, target)
        else:
            if m < target:
                if nums[high] < target:
                    return self.sub_search(nums, low, med, target)
                else:
                    return self.sub_search(nums, med, high, target)
            else:
                return self.sub_search(nums, low, med, target)


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        return self.sub_search(nums, 0, len(nums)-1, target)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([4,5,6,7,0,1,2], 0),
            4
        ),
        (
            ([4,5,6,7,0,1,2], 3),
            -1
        ),
        (
            ([], 0),
            -1
        ),
        (
            ([1,3], 2),
            -1
        )
    ]
    test(Solution().search, test_data)
