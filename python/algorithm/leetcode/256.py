from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        minCostByColor = [0, 0, 0]
        for h in costs:
            c0 = h[0] + min(minCostByColor[1], minCostByColor[2])
            c1 = h[1] + min(minCostByColor[0], minCostByColor[2])
            c2 = h[2] + min(minCostByColor[0], minCostByColor[1])
            minCostByColor = [c0, c1, c2]
        return min(minCostByColor)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [[17,2,17],[16,16,5],[14,3,19]],
            10
        ),
        (
            [[7,6,2]],
            2
        ),
    ]
    test(Solution().minCost, test_data)
