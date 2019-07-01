# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = len(heights)
        if l == 0:
            return 0
        maxArea = 0
        left = [-1]*l
        right = [-1]*l
        for i in range(l):
            p = i - 1
            while p >=0 and heights[p] >= heights[i]:
                p = left[p]
            left[i] = p
        for i in range(l-1, -1, -1):
            p = i + 1
            while p < l and heights[p] >= heights[i]:
                p = right[p]
            right[i] = p
        for i in range(l):
            area = heights[i] * (right[i] - left[i]-1)
            if area > maxArea:
                maxArea = area
        return maxArea


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [2,1,5,6,2,3],
            10
        )
    ]
    test(Solution().largestRectangleArea, test_data)
