# https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/340075/c%2B%2B-beats-100-(both-time-and-memory)-with-algorithm-and-image
# |arr1[i]-arr1[j]| + |arr2[i]-arr2[j]| + |i-j|

# suppose i >= j
# this is equivalent to finding the maximum of the following 4 values

#  arr1[i]-arr1[j] + arr2[i]-arr2[j] + i-j => (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j)
# -arr1[i]+arr1[j] + arr2[i]-arr2[j] + i-j => (arr1[j] - arr2[j] - j) - (arr1[i] - arr2[i] - i)
# arr1[i]-arr1[j] + -arr2[i]+arr2[j] + i-j => (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j)
# -arr1[i]+arr1[j] +-arr2[i]+arr2[j] + i-j => (arr1[j] + arr2[j] - i) - (arr1[i] + arr2[i] - j)
from typing import List

class Solution:
    def max_diff(self, nums):
        max_v = min_v = nums[0]
        for n in nums:
            max_v = max(max_v, n)
            min_v = min(min_v, n)
        return max_v - min_v

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        tmp = [[] for i in range(4)]
        for i, (n1, n2) in enumerate(zip(arr1, arr2)):
            tmp[0].append(n1+n2+i)
            tmp[1].append(n1+n2-i)
            tmp[2].append(n1-n2-i)
            tmp[3].append(n1-n2+i)
        return max(map(self.max_diff, tmp))


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,2,3,4],
                [-1,4,5,6]
            ),
            13
        ),
        (
            (
                [1,-2,-5,0,10],
                [0,-2,-1,-7,-4]
            ),
            20
        ),
    ]
    test(Solution().maxAbsValExpr, test_data)

