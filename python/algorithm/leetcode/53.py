# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

class Solution:
    def maxSubArray(self, nums):
        s = nums[0]
        m = s
        for i in range(1, len(nums)):
            s = s + nums[i] if s > 0 else nums[i]
            m = max(m, s)
        return m

class Solution2:
    def maxSubArray(self, nums):
        s = 0
        minSum = 0
        curSum = 0
        ans = -(1<<31)
        for n in nums:
            curSum += n # sum of the first i+1 nums
            sumOfSubArray = curSum - minSum
            if sumOfSubArray > ans:
                ans = sumOfSubArray
            minSum = min(minSum, curSum)
        return ans

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
        ),
        (
            [3,-1,4],
            6
        )
    ]
    test(Solution().maxSubArray, test_data)
