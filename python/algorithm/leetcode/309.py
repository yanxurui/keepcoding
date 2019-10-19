from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        tab = [0]
        tmp = 0
        for i in range(1, len(prices)):
            for j in range(i-1, -1, -1):
                if prices[j] < prices[i]:
                    # buy at j, sell at i
                    tmp = max(tmp, prices[i]-prices[j]+(tab[j-2] if j >=2 else 0))
            tab.append(tmp)
        return tab[-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [1,2,3,0,2],
            3
        ),
        (
            [3,2,6,5,0,3],
            7
        ),
    ]
    test(Solution().maxProfit, test_data)
