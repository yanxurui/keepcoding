# https://leetcode.com/problems/range-sum-query-mutable/discuss/75724/17-ms-Java-solution-with-segment-tree

from typing import List

class SegTree:
    def __init__(self, nums, i, j):
        self.begin = i
        self.end = j
        self.left = None
        self.right = None
        self.sum = 0

    @classmethod
    def build(cls, nums, b, e):
        if b > e:
            return
        root = cls(nums, b, e)
        if b == e:
            root.sum = nums[b]
        else:
            m = (b + e)//2
            root.left = cls.build(nums, b, m)
            root.right = cls.build(nums, m+1, e)
            root.sum = root.left.sum + root.right.sum
        return root

    def update(self, pos, val):
        if self.begin == self.end:
            assert pos == self.begin
            self.sum = val
        else:
            m = (self.begin + self.end)//2
            if pos <= m:
                self.left.update(pos, val)
            else:
                self.right.update(pos, val)
            self.sum = self.left.sum + self.right.sum
    def sumRange(self, i, j):
        if not (self.begin <= i and self.end >= j):
            return 0
        if self.begin == i and self.end == j:
            return self.sum
        m = (self.begin + self.end)//2
        if i >= m + 1:
            return self.right.sumRange(i, j)
        elif j <= m:
            return self.left.sumRange(i, j)
        else:
            return self.left.sumRange(i, m) + self.right.sumRange(m+1, j)


class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegTree.build(nums, 0, len(nums)-1)

    def update(self, i: int, val: int) -> None:
        self.st.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.st.sumRange(i, j)


nums = [1, 3, 5]
obj = NumArray(nums)
assert obj.sumRange(0, 2) == 9
obj.update(1, 2)
assert obj.sumRange(0, 2) == 8


obj = NumArray([])
