class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        for i in range(1, len(prices)):
            m += max(0, prices[i] - prices[i-1])
        return m

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [7,1,5,3,6,4],
            7
        ),
        (
            [1,2,3,4,5],
            4
        ),
        (
            [7,6,4,3,1],
            0
        ),
    ]
    test(Solution().maxProfit, test_data)
