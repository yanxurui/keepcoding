# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        x = 0
        y = len(matrix[0]) - 1
        while x < len(matrix) and y >=0:
            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                x += 1
            else:
                y -= 1
        return False


if __name__ == '__main__':
    from testfunc import test
    m = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
    test_data = [
        (
            (
                m,
                5
            ),
            True
        ),
        (
            (
                m,
                20
            ),
            False
        ),
        (
            (
                [
                    [1,2],
                    [3,4]
                ],
                2
            ),
            True
        ),
        (
            (
                [
                    [1]
                ],
                2
            ),
            False
        ),
        (
            (
                [
                    [ 1, 3, 5, 7, 9],
                    [ 2, 4, 6, 8,10],
                    [11,13,15,17,19],
                    [12,14,16,18,20],
                    [21,22,23,24,25]
                ],
                13
            ),
            True
        )
    ]
    test(Solution().searchMatrix, test_data)
