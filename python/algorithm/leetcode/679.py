# https://leetcode.com/problems/24-game/discuss/107675/Short-Python

def g_permutations(nums):
    """
    :type nums: List[int], elements in nums can be duplicate, in this case, nums must be sorted
    """
    if len(nums) <= 1:
        yield nums
    else:
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for per in g_permutations(nums[:i]+nums[i+1:]):
                # move i to the head
                # compute permutations of the remaining elements
                yield [nums[i]] + per

def g_combinations(nums, k):
    """
    :type nums: List[int], elements in nums can be duplicate, in this case, nums must be sorted
    """
    if k > len(nums):
        return
    elif k == 0:
        yield []
    elif k == len(nums):
        yield nums
    else:
        i = 1
        while i < len(nums) and nums[i] == nums[0]:
            i += 1
        # the first i eles are the same
        for j in range(min(i, k), -1, -1):
            for com in g_combinations(nums[i:], k-j):
                yield nums[:j] + com

def permutations(nums):
    return list(g_permutations(sorted(nums)))

def combinations(nums, k):
    return list(g_combinations(sorted(nums), k))

import math
import itertools

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        # for a, b, *rest in g_permutations(nums):
        for a, b, *rest in itertools.permutations(nums):
            for c in {a+b, a-b, a*b, b and a/b}:
                if self.judgePoint24([c] + rest):
                    return True
        return False


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [4, 1, 8, 7],
            True
        ),
        (
            [1, 2, 1, 2],
            False
        ),
    ]
    test(Solution().judgePoint24, test_data)


    test_data = [  
        (
            [1,2,3],
            [
                [1,2,3],
                [1,3,2],
                [2,1,3],
                [2,3,1],
                [3,1,2],
                [3,2,1]
            ]
        ),
        (
            [1,2,2],
            [
                [1,2,2],
                [2,1,2],
                [2,2,1]
            ]
        )
    ]
    test(permutations, test_data, unordered_equal)
    test_data = [  
        (
            (
                [1,2,3],
                2
            ),
            [
                [1,2],
                [1,3],
                [2,3]
            ]
        ),
        (
            (
                [1,2,2],
                2
            ),
            [
                [1,2],
                [2,2]
            ]
        )
    ]
    test(combinations, test_data, unordered_equal)

