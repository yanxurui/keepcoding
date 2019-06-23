class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col0 = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # first row
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        # first column
        if col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0


def wrapper(matrix):
    Solution().setZeroes(matrix)
    return matrix

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
                [1,1,1],
                [1,0,1],
                [1,1,1]
            ],
            [
                [1,0,1],
                [0,0,0],
                [1,0,1]
            ]
        ),

        (
            [
                [0,1,2,0],
                [3,4,5,2],
                [1,3,1,5]
            ],
            [
                [0,0,0,0],
                [0,4,5,0],
                [0,3,1,0]
            ]
        )
        ,

        (
            [
                [1,1,1],
                [0,1,2]
            ],
            [
                [0,1,1],
                [0,0,0]
            ]
        )
    ]
    test(wrapper, test_data)
