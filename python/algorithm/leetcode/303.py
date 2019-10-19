from copy import copy
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = copy(nums)
        for i in range(1, len(nums)):
            self._nums[i] += self._nums[i-1]

    def sumRange(self, i: int, j: int) -> int:
        return self._nums[j] - (0 if i == 0 else self._nums[i-1])


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (0, 2),
            1
        ),
        (
            (2, 5),
            -1
        ),
        (
            (0, 5),
            -3
        )
    ]
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    test(obj.sumRange, test_data)
