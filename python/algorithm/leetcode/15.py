 #https://leetcode.com/problems/3sum/discuss/7380/Concise-O(N2)-Java-solution

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rst = []
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                s = 0 - nums[i]
                l = i + 1
                h = len(nums) - 1
                while l < h:
                    if nums[l] + nums[h] == s:
                        rst.append([nums[i], nums[l], nums[h]])
                        while l < h and nums[l] == nums[l+1]:
                            l += 1
                        while l < h and nums[h] == nums[h-1]:
                            h -= 1
                        l += 1
                        h -= 1
                    elif nums[l] + nums[h] < s:
                        l += 1
                    else:
                        h -= 1
        return rst
                            


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            [-1, 0, 1, 2, -1, -4],
            [
              [-1, 0, 1],
              [-1, -1, 2]
            ]
        )
    ]
    test(Solution().threeSum, test_data, compare=unordered_equal)

