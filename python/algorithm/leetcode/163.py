from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        left = lower
        i = 0
        for n in nums:
            if n > left:
                res.append([left, n-1])
            left = n + 1
        if left <= upper:
            res.append([left, upper])
        return res

if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                [0,1,3,50,75],
                0, 99
            ),
            [[2,2],[4,49],[51,74],[76,99]]
        ),
        (
            (
                [-1],
                -1, -1
            ),
            []
        )
    ]
    test(Solution().findMissingRanges, test_data)
