from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                [-1,0,3,5,9,12],
                9
            ),
            4
        ),
        (
            (
                [-1,0,3,5,9,12],
                2
            ),
            -1
        )
    ]
    test(Solution2().search, test_data)
