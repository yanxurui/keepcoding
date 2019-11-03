from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cum_sum = [0]
        for n in nums:
            cum_sum.append(cum_sum[-1]+n)
        for i in range(len(nums)):
            if cum_sum[i] == cum_sum[-1] - cum_sum[i+1]:
                return i
        return -1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1, 7, 3, 6, 5, 6],
            3
        ),
        (
            [-1,-1,-1,0,1,1],
            0
        ),
    ]
    test(Solution().pivotIndex, test_data)

