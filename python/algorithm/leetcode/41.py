# https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time

class Solution(object):
    def swap(self, nums, i, j):
        if nums[i] == nums[j]:
            return False
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        return True

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= n:
                if not self.swap(nums, i, nums[i]-1):
                    break
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return n+1
        

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1,2,0],
            3
        ),
        (
            [3,4,-1,1],
            2
        ),
        (
            [7,8,9,11,12],
            1
        ),
        (
            [-2],
            1
        ),
        (
            [2,1],
            3
        )

    ]
    test(Solution().firstMissingPositive, test_data)
