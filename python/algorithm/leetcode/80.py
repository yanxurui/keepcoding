class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        k = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[k]:
                if nums[i] == nums[k-1]:
                    continue
            k += 1
            nums[k] = nums[i]

        return k+1
        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,1,1,2,2,3],
            5
        ),
        (
            [0,0,1,1,1,1,2,3,3],
            7
        )
    ]
    test(Solution().removeDuplicates, test_data)
