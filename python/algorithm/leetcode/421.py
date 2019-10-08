# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/91049/Java-O(n)-solution-using-bit-manipulation-and-HashMap

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1<<i)
            prefix_set = {(n & mask) for n in nums}
            tmp = rst | (1<<i)
            # assume p, q in prefix_set such that p^q = tmp
            # q = p^tmp
            for p in prefix_set:
                if (tmp^p) in prefix_set:
                    rst = tmp
                    break
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ([3, 10, 5, 25, 2, 8]),
            28
        )
    ]
    test(Solution().findMaximumXOR, test_data)
