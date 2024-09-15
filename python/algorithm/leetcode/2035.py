from typing import List

# Time Limit Exceeded
class Solution:
    def backtrack(self, nums, i, cntNeeded, t, curSum):
        '''
        pick cntNeeded numbers from nums[i:] such that the sum is closest to t
        '''
        if cntNeeded == 0:
            return abs(t-curSum)
        if i >= len(nums):
            return (1<<31)-1
        # pick i or not
        return min(
            self.backtrack(nums, i+1, cntNeeded-1, t, curSum+nums[i]),
            self.backtrack(nums, i+1, cntNeeded, t, curSum))

    def minimumDifference(self, nums: List[int]) -> int:
        cntNeeded = len(nums)//2
        t = sum(nums)/2
        return 2 * self.backtrack(nums, 0, cntNeeded, t, 0)


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [  
        (
            [3,9,7,3],
            2
        ),
        (
            [-36,36],
            72
        ),
        (
            [2,-1,0,4,-2,-9],
            0
        ),
        (
            [7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694],
            0
        )
    ]
    test(Solution().minimumDifference, test_data)

