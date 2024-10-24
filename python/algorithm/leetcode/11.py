from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        rst = 0
        i, j = 0, n-1
        while i < j:
            width = j - i
            short = min(height[i], height[j])
            area = short * width
            rst = max(rst, area)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return rst



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1,8,6,2,5,4,8,3,7],
            49
        )
    ]
    test(Solution().maxArea, test_data)

