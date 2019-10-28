
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # 1. Find the largest index k such that nums[k] < nums[k + 1].
        k = n-2
        while k>=0:
            if nums[k] < nums[k+1]:
                break
            k -= 1
        # If no such index exists, just reverse nums and done.
        if k == -1:
            nums.sort()
        # 2. Find the largest index l > k such that nums[k] < nums[l].
        else:
            for l in range(n-1, k, -1):
                if nums[l] > nums[k]:
                    break
            tmp = nums[l]
            nums[l] = nums[k]
            nums[k] = tmp
            nums[k+1:] = sorted(nums[k+1:])
        return


# https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia
class Solution2(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # 1. Find the largest index k such that nums[k] < nums[k + 1].
        k = n-2
        while k>=0:
            if nums[k] < nums[k+1]:
                break
            k -= 1
        # If no such index exists, just reverse nums and done.
        if k == -1:
            nums.sort()
        # 2. Find the largest index l > k such that nums[k] < nums[l].
        else:
            for l in range(n-1, k, -1):
                if nums[l] > nums[k]:
                    break
            tmp = nums[l]
            nums[l] = nums[k]
            nums[k] = tmp
            nums[k+1:] = sorted(nums[k+1:])
        return

def wrapper(nums):
    Solution2().nextPermutation(nums)
    return nums

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1,2,3],
            [1,3,2]
        ),
        (
            [3,2,1],
            [1,2,3]
        ),
        (
            [1,1,5],
            [1,5,1]
        ),
        (
            [1,2,3,4],
            [1,2,4,3]
        ),
        (
            [1,2,4,3],
            [1,3,2,4]
        ),
        (
            [1,3,2,4],
            [1,3,4,2]
        ),
        (
            [1,3,4,2],
            [1,4,2,3]
        ),
        (
            [1,2],
            [2,1]
        )
    ]
    test(wrapper, test_data)
    test(wrapper, [(
            [1,2],
            [2,1]
        )])
