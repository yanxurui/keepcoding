from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        rst = [None] * len(nums)
        # from right to left
        stack = [] # decreasing
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i]>=stack[-1]:
                stack.pop()
            if stack:
                rst[i] = stack[-1]
            stack.append(nums[i])
        # from left to right
        stack = [] # increasing
        for i in range(len(nums)):
            if rst[i] is None:
                j = self.bs(stack, nums[i])
                if j < len(stack):
                    rst[i] = stack[j]
                else:
                    rst[i] = -1
            if not stack or nums[i] > stack[-1]:
                stack.append(nums[i])
        return rst

    def bs(self, nums, target):
        # find the index of the first ele that is greater than target
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l

# https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice
class Solution2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        rst = [-1] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                rst[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                rst[stack.pop()] = nums[i]
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,2,1],
            [2,-1,2]
        ),
        (
            [1,8,-1,-100,-1,222,1111111,-111111],
            [8,222,222,-1,222,1111111,-1,1]
        ),
    ]
    test(Solution2().nextGreaterElements, test_data)

