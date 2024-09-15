from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums)-2):
            newTarget = target - nums[i]
            if 2 * nums[i] >= newTarget:
                break
            j = i + 1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] >= newTarget:
                    k -= 1
                else:
                    ans += (k-j)
                    j += 1
        return ans

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [-2,0,1,3],
                2
            ),
            2
        ),
        (
            (
                [],
                0
            ),
            0
        ),
        (
            (
                [0],
                0
            ),
            0
        ),
    ]
    test(Solution().threeSumSmaller, test_data)

