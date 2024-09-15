# https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # k=3, p=1
        # -> m = 2, k=11, mask = ~(x1 & x2)
        x1 = 0
        x2 = 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x1 &= mask
            x2 &= mask
        return x1 # p=01

# https://leetcode.com/problems/single-number-ii/solutions/43294/challenge-me-thx/
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = 0
        twos = 0
        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones
        return ones


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            ([2,2,3,2]),
            3
        ),
        (
            ([0,1,0,1,0,1,99]),
            99
        )
    ]
    test(Solution2().singleNumber, test_data)
