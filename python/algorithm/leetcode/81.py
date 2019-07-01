class Solution(object):
    def sub_search(self, nums, low, high, target):
        med = (low + high)/2
        m = nums[med]
        if m == target:
            return True
        if med == low:
            if nums[high] == target:
                return True
            else:
                return False
        if m > nums[low]:
            if m < target:
                return self.sub_search(nums, med, high, target)
            else:
                if nums[low] > target:
                    return self.sub_search(nums, med, high, target)
                else:
                    return self.sub_search(nums, low, med, target)
        elif m < nums[low]:
            if m < target:
                if nums[high] < target:
                    return self.sub_search(nums, low, med, target)
                else:
                    return self.sub_search(nums, med, high, target)
            else:
                return self.sub_search(nums, low, med, target)
        else:
            while low < len(nums)-1 and low < high  and nums[low] == nums[low+1]:
                low += 1
            while high > 0 and low < high and nums[high] == nums[high-1]:
                high -= 1
            return self.sub_search(nums, low, high, target)


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        return self.sub_search(nums, 0, len(nums)-1, target)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [2,5,6,0,0,1,2],
                0
            ),
            True
        ),
        (
            (
                [2,5,6,0,0,1,2],
                3
            ),
            False
        ),
        (
            (
                [1,1,3,1],
                3
            ),
            True
        )
    ]
    test(Solution().search, test_data)
