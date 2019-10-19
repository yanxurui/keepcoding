from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        rst = [0] * l
        nums_sorted = []
        for i in range(len(nums)-1, -1, -1):
            rst[i] = self.insert(nums_sorted, nums[i])
        return rst

    def insert(self, nums, t):
        p = self.bs(nums, 0, len(nums)-1, t)
        if p == -1:
            p = len(nums)
        nums.insert(p, t)
        return p

    def bs(self, nums, b, e, t):
        # find the first one that is larger or equal than t
        if b > e:
            return -1
        m = (b+e)//2
        if nums[m] >= t:
            tmp = self.bs(nums, b, m-1, t)
            return tmp if tmp >= 0 else m
        else:
            return self.bs(nums, m+1, e, t)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [5,2,6,1],
            [2,1,1,0]
        ),
        (
            [1,2,3,4],
            [0,0,0,0]
        ),
        (
            [4,3,2,1],
            [3,2,1,0]
        ),
    ]
    test(Solution().countSmaller, test_data)
