class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = (left + right) / 2
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                break
        if left > right:
            return False

        row = matrix[mid]

        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left + right) / 2
            if target < row[mid]:
                right = mid - 1
            elif target > row[mid]:
                left = mid + 1
            else:
                return True
        return False




        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [
                    [1,   3,  5,  7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50]
                ],
                3
            ),
            True
        ),

        (
            (
                [
                    [1,   3,  5,  7],
                    [10, 11, 16, 20],
                    [23, 30, 34, 50]
                ],
                13
            ),
            False
        ),
        (
            (
                [[]],
                1
            ),
            False
        )
    ]
    test(Solution().searchMatrix, test_data)
