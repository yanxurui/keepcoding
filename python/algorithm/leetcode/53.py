# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

class Solution:
    def maxSubArray(self, nums):
        s = nums[0]
        m = s
        for i in range(1, len(nums)):
            s = s + nums[i] if s > 0 else nums[i]
            m = max(m, s)
        return m

if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [-2,1,-3,4,-1,2,1,-5,4],
            6
        ),
        (
            [-1, -2],
            -1
        )
    ]
    test(Solution().maxSubArray, test_data)
