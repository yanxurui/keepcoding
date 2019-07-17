class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0]
        m = 0
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            else:
                if prices[i] - low > m:
                    m = prices[i] - low
        return m

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [7,1,5,3,6,4],
            5
        ),
        (
            [7,6,4,3,1],
            0
        ),
    ]
    test(Solution().maxProfit, test_data)
