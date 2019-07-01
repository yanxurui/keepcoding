def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

class Solution(object):

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = -1
        two = len(nums)
        i = 0
        while i < two:
            if nums[i] == 0:
                zero += 1
                if i > zero:
                    swap(nums, i, zero)
                    continue
            elif nums[i] == 2:
                two -= 1
                if i < two:
                    swap(nums, i, two)
                    continue
            i += 1


def wrapper(nums):
    Solution().sortColors(nums)    
    return nums


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [2,0,2,1,1,0],
            [0,0,1,1,2,2]
        ),
        (
            [0,1,2,0],
            [0,0,1,2]
        )
    ]
    test(wrapper, test_data)
