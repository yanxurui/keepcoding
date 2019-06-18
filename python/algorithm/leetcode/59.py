class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[n*n for i in range(n)] for i in range(n)]
        start = 0
        num = 1
        while start <= n/2:
            end = n - start - 1
            i = start
            # up
            for j in range(start, end):
                ans[i][j] = num
                num += 1
            # end
            for i in range(start, end):
                ans[i][end] = num
                num += 1
            # bottom
            for j in range(end, start, -1):
                ans[end][j] = num
                num += 1
            # start
            for i in range(end, start, -1):
                ans[i][start] = num
                num += 1
            start += 1
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            3,
            [
                [ 1, 2, 3 ],
                [ 8, 9, 4 ],
                [ 7, 6, 5 ]
            ]
        ),
        (
            2,
            [
                [1,2],
                [4,3]
            ]
        ),
        (
            1,
            [
                [1]
            ]
        )
    ]
    test(Solution().generateMatrix, test_data)
