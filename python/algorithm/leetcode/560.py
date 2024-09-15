from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = defaultdict(int)
        d[0] = 1 # empty subarry, very important
        rst = 0
        prev = 0
        for i in range(len(nums)):
            s = prev + nums[i] # sum of the first i+1 eles
            rst += d[s-k]
            d[s] += 1
            prev = s
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,1,1],
                2
            ),
            2
        )
    ]
    test(Solution().subarraySum, test_data)

