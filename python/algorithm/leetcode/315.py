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
        nums.insert(p, t)
        return p

    def bs(self, nums, l, r, t):
        # find the first one that is larger than or equal to t
        while l <= r:
            m = l + (r-l)//2
            if nums[m] >= t:
                r = m - 1
            else:
                l = m + 1
        return l
        


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
