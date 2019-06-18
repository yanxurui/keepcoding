class Solution(object):
    def maxmin(self, m1, m2, func):
        if m1 is not None and m2 is not None:
            return func(m1, m2)
        elif m1 is not None:
            return m1
        elif m2 is not None:
            return m2
        else:
            raise Exception('both are Nones')

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        overall run time complexity should be O(log (m+n))
        """
        n = len(nums1) + len(nums2)
        i, j = 0, 0
        while i+j < n//2: # i+j is the number of numbers that have been processed
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    i += 1
                else:
                    j += 1
            elif i < len(nums1):
                i += 1
            else:
                assert j < len(nums2)
                j += 1

        if n % 2 == 1:
            m1, m2 = None, None
            if i < len(nums1):
                m1 = nums1[i]
            if j < len(nums2):
                m2 = nums2[j]
            m = self.maxmin(m1, m2, min)
        else:
            m1, m2 = None, None
            if i-1 >= 0:
                m1 = nums1[i-1]
            if j-1 >= 0:
                m2 = nums2[j-1]
            left = self.maxmin(m1, m2, max)

            m1, m2 = None, None
            if i < len(nums1):
                m1 = nums1[i]
            if j < len(nums2):
                m2 = nums2[j]
            right = self.maxmin(m1, m2, min)
            m = (left + right)/2.0
        return m


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

