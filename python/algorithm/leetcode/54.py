# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby

class Solution:
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])

class Solution2:
    def spiralOrder(self, matrix):
        n = len(matrix)
        if n > 0:
            m = len(matrix[0])
        if n == 0 or m == 0:
            return []
        rst = []
        up, down = 0, n-1
        left, right = 0, m-1
        while up <= down and left <= right:
            # traverse right
            for i in range(left, right+1):
                rst.append(matrix[up][i])
            up += 1
            
            # traverse down
            for i in range(up, down+1):
                rst.append(matrix[i][right])
            right -= 1

            # traverse left
            # we need extra check to avoid duplicate
            if up <= down:
                for i in range(right, left-1, -1):
                    rst.append(matrix[down][i])
                down -= 1

            # traverse up
            if left <= right:
                for i in range(down, up-1, -1):
                    rst.append(matrix[i][left])
                left += 1
        return rst

if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            [
                [ 1, 2, 3 ],
                [ 4, 5, 6 ],
                [ 7, 8, 9 ]
            ],
            [1,2,3,6,9,8,7,4,5]
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9,10,11,12]
            ],
            [1,2,3,4,8,12,11,10,9,5,6,7]
        ),

        (
            [],
            []
        )
    ]
    test(Solution2().spiralOrder, test_data)
