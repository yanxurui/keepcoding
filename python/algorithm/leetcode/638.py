import sys
INT_MAX = sys.maxsize
from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        rst = INT_MAX
        # use offers
        for sp in special:
            left = self.diff(needs, sp)
            if left is None:
                continue
            rst = min(rst, sp[-1] + self.shoppingOffers(price, special, left))
        # do not use offers
        rst = min(rst, sum([price[i]*n for i,n in enumerate(needs)]))
        return rst

    def diff(self, needs, offer):
        rst = list(needs)
        i = 0
        while i < len(rst):
            if offer[i] > rst[i]:
                return None
            rst[i] -= offer[i]
            i += 1
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [2,5], [[3,0,5],[1,2,10]], [3,2]
            ),
            14
        ),
        (
            (
                [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
            ),
            11
        ),
    ]
    test(Solution().shoppingOffers, test_data)

