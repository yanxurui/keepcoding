from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            idx = abs(n)-1
            nums[idx] = -abs(nums[idx])
        rst = []
        for i in range(len(nums)):
            if nums[i] > 0:
                rst.append(i+1)
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [4,3,2,7,8,2,3,1],
            [5, 6]
        )
    ]
    test(Solution().findDisappearedNumbers, test_data)

