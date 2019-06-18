class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-1-i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp

def wrapper(matrix):
    Solution().rotate(matrix)
    return matrix


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ],
            [
                [7,4,1],
                [8,5,2],
                [9,6,3]
            ]
        ),
        (
            [
                [ 5, 1, 9,11],
                [ 2, 4, 8,10],
                [13, 3, 6, 7],
                [15,14,12,16]
            ],
            [
                [15,13, 2, 5],
                [14, 3, 4, 1],
                [12, 6, 8, 9],
                [16, 7,10,11]
            ]
        )
    ]
    test(wrapper, test_data)

