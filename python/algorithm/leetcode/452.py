# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93703/Share-my-explained-Greedy-solution
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        rst = 1
        points = sorted(points, key=lambda item:item[1])
        arrow = points[0][1]
        for i in range(1, len(points)):
            if arrow >= points[i][0]:
                continue
            arrow = points[i][1]
            rst += 1
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[10,16], [2,8], [1,6], [7,12]],
            2
        )
    ]
    test(Solution().findMinArrowShots, test_data)

