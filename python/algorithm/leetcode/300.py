#coding=utf-8
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        if len(nums) == 0:
            return 0
        tab = []
        for i in range(len(nums)):
            tmp = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, tab[j] + 1)
            tab.append(tmp)
        return max(tab)

# https://leetcode.com/problems/longest-increasing-subsequence/solutions/74824/java-python-binary-search-o-nlogn-time-with-explanation/
# N*logN
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        def bs(nums, t):
            # return the first i such that nums[i] > t
            l = 0
            r = len(nums)-1
            while l <= r:
                m = (l+r)//2
                if t >= nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            return l

        smallestTailWithLengthI = []
        for n in nums:
            i = bs(smallestTailWithLengthI, n)
            if i == len(smallestTailWithLengthI):
                smallestTailWithLengthI.append(n)
            else:
                smallestTailWithLengthI[i] = n
        return len(smallestTailWithLengthI)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [10,9,2,5,3,7,101,18],
            4
        )
    ]
    test(Solution2().lengthOfLIS, test_data)
