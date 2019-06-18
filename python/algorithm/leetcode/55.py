class Solution:
    def __init__(self):
        self.table = {}

    def canJump(self, nums):
        n = len(nums)
        if n == 1:
            return True
        if not (0 in nums):
            return True
        assert n > 1
        if n-1 in self.table:
            return self.table[n-1]
        ans = False
        import pdb
        # pdb.set_trace()
        for j in range(n-2, -1, -1):
            if nums[j] >= n - 1 - j:
                if self.canJump(nums[:j+1]):
                    ans = True
                    break
        self.table[n-1] = ans
        return ans


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
