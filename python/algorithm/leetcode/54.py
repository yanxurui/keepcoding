# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby

class Solution:
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])


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
    test(Solution().spiralOrder, test_data)
