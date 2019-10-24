from typing import List

def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        while True:
            while i <= j and nums[i] != val:
                i += 1
            while i <= j and nums[j] == val:
                j -= 1
            if i > j:
                break
            else:
                swap(nums, i, j)
                i += 1
                j -= 1
        return j+1


def wrapper(nums, val):
    n = Solution().removeElement(nums, val)
    return n, nums[:n]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [3,2,2,3],
                3
            ),
            (2, [2,2])
        ),
        (
            (
                [0,1,2,2,3,0,4,2],
                2
            ),
            (5, [0,1,4,0,3])
        ),
        
    ]
    test(wrapper, test_data)
