# https://leetcode.com/problems/subarray-sums-divisible-by-k/solutions/217985/java-c-python-prefix-sum/
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = [0] * k
        count[0] = 1
        ans = 0
        for n in nums:
            prefix = (prefix + n) % k
            ans += count[prefix]
            count[prefix] += 1
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [4,5,0,-2,-3,1],
                5
            ),
            7
        ),
        (
            (
                [5],
                9
            ),
            0
        ),
    ]
    test(Solution().subarraysDivByK, test_data)

