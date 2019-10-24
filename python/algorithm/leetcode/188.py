# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java

class Solution:
    def maxProfit(self, k, prices) -> int:
        l = len(prices)
        if k > l//2:
            return self.quickSolver(prices)
        tab = [[0 for y in range(l)] for x in range(k+1)]
        for t in range(1,k+1):
            maxTemp = -prices[0]
            for j in range(1, l):
                tab[t][j] = max(tab[t][j-1], prices[j]+maxTemp)
                maxTemp = max(maxTemp, tab[t-1][j-1]-prices[j]) # buy at j
        return tab[k][l-1]

    def quickSolver(self, prices):
        prof = 0
        for i in range(1, len(prices)):
            d = prices[i] - prices[i-1]
            if d > 0:
                prof += d
        return prof


import sys
INT_MAX = sys.maxsize
INT_MIN = -INT_MAX-1

class Solution2:
    def maxProfit(self, k, prices) -> int:
        if k >= len(prices)//2:
            return self.quickSolver(prices)

        tmp = [[INT_MIN, 0] for i in range(k+1)]
        # tmp[i] means the max money after buy or sell the i-th time
        for p in prices:
            for i in range(1, k+1):
                tmp[i][0] = max(tmp[i][0], tmp[i-1][1] - p) # buy at p
                tmp[i][1] = max(tmp[i][1], tmp[i][0] + p) # sell at p
        return tmp[k][1]
    
    def quickSolver(self, prices):
        prof = 0
        for i in range(1, len(prices)):
            d = prices[i] - prices[i-1]
            if d > 0:
                prof += d
        return prof

if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (
                2,
                [2,4,1]
            ),
            2
        ),
        (
            (
                2,
                [3,2,6,5,0,3]
            ),
            7
        ),
        (
            (
                1,
                [6,1,6,4,3,0,2]
            ),
            5
        ),
        (
            (
                2,
                [1,2,4]
            ),
            3
        ),
        (
            (
                2,
                [1,2,4,2,5,7,2,4,9,0]
            ),
            13
        ),
        (
            (
                2,
                []
            ),
            0
        ),
        (
            (
                0,
                [1,3]
            ),
            0
        )
    ]
    test(Solution2().maxProfit, test_data)
