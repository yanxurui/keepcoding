# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, hold2 = float('-inf'), float('-inf')
        release1, release2 = 0, 0
        import pdb
        pdb.set_trace()
        for p in prices:
            hold1 = max(hold1, -p)
            release1 = max(release1, hold1+p)
            hold2 = max(hold2, release1-p)
            release2 = max(release2, hold2+p)
        return release2


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        # (
        #     [3,3,5,0,0,3,1,4],
        #     6
        # ),
        # (
        #     [1,2,3,4,5],
        #     4
        # ),
        # (
        #     [7,6,4,3,1],
        #     0
        # ),
        (
            [2,3,1,4,3],
            4
        )
    ]
    test(Solution().maxProfit, test_data)
