from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,2,2,1],
                [2,2]
            ),
            [2]
        ),
        (
            (
                [4,9,5],
                [9,4,9,8,4]
            ),
            [9,4]
        ),
    ]
    test(Solution().intersection, test_data)

