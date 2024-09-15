# https://leetcode.com/problems/rotate-array/discuss/54252/Java-O(1)-space-solution-of-Rotate-Array.

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 0:
            return
        k %= l
        if k == 0:
            return
        #    [1,2,3,4,5,6,7]
        # => [4,3,2,1,7,6,5]
        # => [5,6,7,1,2,3,4]
        self.reverse(nums, 0, l-k-1)
        self.reverse(nums, l-k, l-1)
        self.reverse(nums, 0, l-1)

    def reverse(self, nums, b, e):
        while b < e:
            tmp = nums[b]
            nums[b] = nums[e]
            nums[e] = tmp
            b += 1
            e -= 1

def wrapper(nums, k):
    Solution().rotate(nums, k)
    return nums


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                [1,2,3,4,5,6,7],
                3
            ),
            [5,6,7,1,2,3,4]
        ),
        (
            (
                [-1,-100,3,99],
                2
            ),
            [3,99,-1,-100]
        )
    ]
    test(wrapper, test_data)
