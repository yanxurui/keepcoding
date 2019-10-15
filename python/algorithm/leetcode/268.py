from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        # (
        #     [3,0,1],
        #     2
        # ),
        (
            [9,6,4,2,3,5,7,0,1],
            8
        ),
        (
            [0,1],
            2
        ),
    ]
    test(Solution().missingNumber, test_data)
