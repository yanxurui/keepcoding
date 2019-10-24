# -*- coding:utf-8 -*-
class Box:
    def getHeight(self, w, l, h, n):
        # write code here
        def get(i):
            if dp[i] != -1:
                return dp[i]
            dp[i] = h[i]
            for j in range(n):
                if w[j] < w[i] and l[j] < l[i]:
                    dp[i] = max(dp[i], get(j)+h[i])
            return dp[i]

        dp = [-1] * n
        rst = -1
        for i in range(n):
            rst = max(rst, get(i))
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,1,1],[1,1,1],[1,1,1], 3
            ),
            1
        )
    ]
    test(Box().getHeight, test_data)
