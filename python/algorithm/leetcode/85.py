class Solution(object):
    def maximalHist(self, heights):
        maxArea = 0
        l = len(heights)
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

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxArea = 0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0] * len(matrix[0])
        for row in matrix:
            for i, cell in enumerate(row):
                if cell == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            maxArea = max(maxArea, self.maximalHist(heights))
        return maxArea
        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
              ["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]
            ],
            6
        )
    ]
    test(Solution().maximalRectangle, test_data)
