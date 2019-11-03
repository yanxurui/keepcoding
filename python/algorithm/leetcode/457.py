from typing import List

# https://leetcode.com/problems/circular-array-loop/discuss/94148/Java-SlowFast-Pointer-Solution
class Solution2:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        jump = lambda i: (i + nums[i]) % len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            slow = fast = i
            while nums[fast] * nums[i] > 0 and nums[jump(fast)] * nums[i] > 0:
                slow = jump(slow)
                fast = jump(jump(fast))
                if slow == fast:
                    if slow == jump(slow):
                        break
                    else:
                        return True

            # mark as 0 to accelerate, will not trap in self-loop
            slow = i
            while nums[slow] * nums[i] > 0:
                nums[slow] = 0
                slow = jump(slow)
        return False

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            j = i
            cnt = 1
            while nums[j] * nums[i] > 0:
                # keep direction
                to = (j + nums[j]) % len(nums)
                if to == j:
                    break
                if to == i:
                    return True
                if cnt >= len(nums):
                    # traped in a loop not including i
                    return True
                j = to
                cnt += 1
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [2,-1,1,2,2],
            True
        ),
        (
            [-1,2],
            False
        ),
        (
            [-2,1,-1,-2,-2],
            False
        ),
        (
            [1,1,2],
            True
        )
    ]
    test(Solution2().circularArrayLoop, test_data)

