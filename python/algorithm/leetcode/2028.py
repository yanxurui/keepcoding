from typing import List
class Solution2:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean * (len(rolls) + n) - sum(rolls)
        if target < n or target > 6 * n:
            return []
        x = target // n
        y = target % n
        ans = [x] * n
        for i in range(y):
            ans[i] += 1
        return ans

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = mean * (len(rolls) + n)
        target = s - sum(rolls)
        return self.KSum([i for i in range(1, 7)], 0, n, [], target)

    def KSum(self, nums, i, k, tmp, target):
        assert k >= 0
        assert target >= 0
        if k == 0:
            if target == 0:
                # succeeded
                return tmp
            else:
                # failed
                return []
        # starting from i since a number can be taken for more than once
        for j in range(i, len(nums)):
            if nums[j] <= target:
                a = self.KSum(nums, j, k-1, tmp+[nums[j]], target-nums[j])
                if a:
                    return a
        return []

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [3,2,4,3],
                4,
                2
            ),
            [6, 6]
        ),
        (
            (
                [1,5,6],
                3,
                4
            ),
            [1, 1, 1, 6]
        ),
        (
            (
                [1,2,3,4],
                6,
                4
            ),
            []
        )
    ]
    test(Solution().missingRolls, test_data)

