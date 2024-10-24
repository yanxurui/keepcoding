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
            if n not in d: # this is important
                # if left > 1
                # e.g., left is 2
                # we have n-2, n-1
                # not n-1, n
                # because n does not in d
                left = d.get(n-1, 0)
                right = d.get(n+1, 0)
                # length of sequence that begins or ends with n
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
            [100, 4, 200, 1, 3, 2],
            4
        ),
        (
            [1,3,2,2],
            3
        )
    ]
    test(Solution().longestConsecutive, test_data)
