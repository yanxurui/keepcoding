# -*- coding:utf-8 -*-

class Stack:
    def getHeight(self, actors, n):
        # write code here
        dp = [0] * n
        rst = 0
        for i in range(n):
            rst = max(rst, self.get(dp, actors, i))
        return rst

    def get(self, dp, actors, i):
        # get the largest height when actor i is on the top
        if dp[i] > 0:
            return dp[i]
        dp[i] = 1
        for j in range(len(actors)):
            if i == j:
                continue
            if actors[i][0] < actors[j][0] and actors[i][1] < actors[j][1]:
                # i stand on top of j
                dp[i] = max(dp[i], self.get(dp, actors, j)+1)
        return dp[i]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [[1,2],[3,4],[5,6],[7,8]],4
            ),
            4
        )
    ]
    test(Stack().getHeight, test_data)
