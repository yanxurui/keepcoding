class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        ma, mi = res, res
        for n in nums[1:]:
            if n < 0:
                # a negative value makes a big num smaller, a small num bigger
                tmp = ma
                ma = mi
                mi = tmp
            ma = max(ma * n, n)
            mi = min(mi * n, n)
            res = max(res, ma)
        return res

        
if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ([2,3,-2,4]),
            6
        ),
        (
            ([-2,0,-1]),
            0
        ),
        (
            ([-1]),
            -1
        ),
        (
            ([-2,3,-4]),
            24
        ),
        (
            ([-1,-2,-9,-6]),
            108
        )
    ]
    test(Solution().maxProduct, test_data)

