from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rst = [1] * n
        tmp = 1
        for i in range(n):
            rst[i] *= tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(n-1, -1, -1):
            rst[i] *= tmp
            tmp *= nums[i]
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1,2,3,4],
            [24,12,8,6]
        )
    ]
    test(Solution().productExceptSelf, test_data)
