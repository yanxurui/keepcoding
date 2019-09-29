# https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O(n)-and-O(n-log-n)-solution

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums) + 1
        left = 0
        total = 0
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right-left+1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0
        

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                7,
                [2,3,1,2,4,3]
            ),
            2
        ),
        (
            (
                10,
                [1,2,3]
            ),
            0
        )
    ]
    test(Solution().minSubArrayLen, test_data)
