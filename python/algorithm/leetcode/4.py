# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2496/Concise-JAVA-solution-based-on-Binary-Search

import sys
INT_MAX = sys.maxsize

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        overall run time complexity should be O(log (m+n))
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0 and n == 0:
            return 0
        if (m+n)%2 == 0:
            return (self.findKth(nums1, 0, nums2, 0, (m+n)//2) + self.findKth(nums1, 0, nums2, 0, (m+n)//2+1))/2
        else:
            return self.findKth(nums1, 0, nums2, 0, (m+n)//2+1)

    def findKth(self, nums1, start1, nums2, start2, k):
        if start1 >= len(nums1):
            return nums2[start2+k-1]
        if start2 >= len(nums2):
            return nums1[start1+k-1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        mid1, mid2 = INT_MAX, INT_MAX
        m = k//2 # k=4, m=2; k=5, m=2
        if start1 + m - 1 < len(nums1):
            mid1 = nums1[start1+m-1]
        if start2 + m - 1 < len(nums2):
            mid2 = nums2[start2+m-1]
        if mid1 < mid2:
            return self.findKth(nums1, start1+m, nums2, start2, k-m)
        else:
            return self.findKth(nums1, start1, nums2, start2+m, k-m)

        
        


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                [1, 3],
                [2]
            ),
            2
        ),
        (
            (
                [1, 2],
                [3, 4]
            ),
            2.5
        ),

        (
            (
                [1],
                []
            ),
            1
        ),
        (
            (
                [3,4],
                []
            ),
            3.5
        )

    ]
    test(Solution().findMedianSortedArrays, test_data)

