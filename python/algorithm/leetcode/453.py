from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # support in m moves, every number increases to x
        # we have 2 equatons:
        # len(nums) * x = S + m * (len(nums)-1)
        # m = x - min(nums)
        # we get:
        # m = S - min
        return sum(nums) - len(nums)*min(nums)
                            


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [1,2,3],
            3
        ),
        (
            [1,1,1],
            0
        )
    ]
    test(Solution().minMoves, test_data)

