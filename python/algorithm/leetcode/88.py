class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def wrapper(nums1, *args):
    Solution().merge(nums1, *args)
    return nums1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,2,3,0,0,0], 3,
                [2,5,6], 3
            ),
            [1,2,2,3,5,6]
        )
    ]
    test(wrapper, test_data)
