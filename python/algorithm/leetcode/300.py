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


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [10,9,2,5,3,7,101,18],
            4
        )
    ]
    test(Solution().lengthOfLIS, test_data)
