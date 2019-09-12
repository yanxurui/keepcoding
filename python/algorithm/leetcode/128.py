# https://leetcode.com/problems/longest-consecutive-sequence/discuss/41055/My-really-simple-Java-O(n)-solution-Accepted
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        res = 0
        for n in nums:
            if n not in d:
                left = d.get(n-1, 0)
                right = d.get(n+1, 0)
                # length of sequence that contains n, might be wrong if it is in the middle of a sequence
                s = left + right + 1
                res = max(res, s)
                d[n] = s
                d[n-left] = s
                d[n+right] = s
        return res


if __name__ == '__main__':
    from testfunc import test
    test_data = [  
        (
            (
                [100, 4, 200, 1, 3, 2]
            ),
            4
        )
    ]
    test(Solution().longestConsecutive, test_data)
