# https://leetcode.com/problems/single-number/discuss/42997/My-O(n)-solution-using-XOR

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            ([2,2,1]),
            1
        ),
        (
            ([4,1,2,1,2]),
            4
        )
    ]
    test(Solution().singleNumber, test_data)
