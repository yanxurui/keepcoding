from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # two pointers
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        rst = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                rst.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return rst

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rst = []
        count = Counter(nums1)
        for n in nums2:
            if count.get(n, 0) > 0:
                rst.append(n)
                count[n] -= 1
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal

    test_data = [  
        (
            (
                [1,2,2,1],
                [2,2]
            ),
            [2, 2]
        ),
        (
            (
                [4,9,5],
                [9,4,9,8,4]
            ),
            [4,9]
        ),
    ]
    test(Solution().intersect2, test_data, compare=unordered_equal)

