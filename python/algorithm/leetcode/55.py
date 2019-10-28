class Solution:
    def canJump(self, nums):
        reach = 0
        i = 0
        while i < len(nums) and i <= reach:
            reach = max(reach, i+nums[i])
            if reach >= len(nums)-1:
                return True
            i += 1
        return False


def wrapper(nums):
    return Solution().canJump(nums)

if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [2,3,1,1,4],
            True
        ),
        (
            [3,2,1,0,4],
            False
        )
    ]
    test(wrapper, test_data)
