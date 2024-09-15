from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        assert p > 0
        assert len(nums) > 0
        # binary search
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            med = (left + right) // 2
            # try to find p pairs such that the max-min diff is <= med
            k = 0
            i = 1
            while i < len(nums):
                # (i-1, i)
                d = nums[i] - nums[i-1]
                if d > med:
                    # try (i+1, i)
                    i += 1
                else:
                    # try (i+1, i+2)
                    i += 2
                    k += 1
                    if k >= p:
                        break
            if k >= p:
                # found!
                # med is too large, try a smaller one
                right = med
            else:
                # failed to find, try a larger one
                left = med + 1
        return left

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [10,1,2,7,1,3],
                2
            ),
            1
        ),
        (
            (
                [4,2,1,2],
                1
            ),
            0
        ),
        (
            (
                [3,4,2,3,2,1,2],
                3
            ),
            1
        )
    ]
    test(Solution().minimizeMax, test_data)
