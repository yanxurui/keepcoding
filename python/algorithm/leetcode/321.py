# https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def sub(nums, k):
            out = []
            drop = len(nums) - k
            for num in nums:
                while drop and out and num > out[-1]:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1)+len(nums2))]

        tmp = []
        for i in range(max(0, k-len(nums2)), min(len(nums1), k)+1):
            j = k - i
            tmp.append(merge(sub(nums1, i), sub(nums2, j)))
        return max(tmp)

        
if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [3, 4, 6, 5],
                [9, 1, 2, 5, 8, 3],
                5
            ),
            [9, 8, 6, 5, 3]
        ),
        (
            (
                [6, 7],
                [6, 0, 4],
                5
            ),
            [6, 7, 6, 0, 4]
        ),
        (
            (
                [6, 0, 4],
                [6, 7],
                5
            ),
            [6, 7, 6, 0, 4]
        ),
        (
            (
                [3, 9],
                [8, 9],
                3
            ),
            [9, 8, 9]
        ),
        (
            (
                [6,7,5],
                [4,8,1],
                3
            ),
            [8,7,5]
        )
    ]
    test(Solution().maxNumber, test_data)

