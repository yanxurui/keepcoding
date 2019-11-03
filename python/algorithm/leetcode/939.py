# https://leetcode.com/problems/minimum-area-rectangle/discuss/192021/Python-O(N1.5)-80ms
from typing import List
INT_MAX = 1<<31-1
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = INT_MAX
        seen = set()
        for x1,y1 in points:
            for x2,y2 in seen:
                if (x1,y2) in seen and (x2,y1) in seen:
                    a = abs(x1-x2)*abs(y1-y2)
                    if a > 0:
                        area = min(area, a)
            seen.add((x1,y1))
        return area if area < INT_MAX else 0


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[1,1],[1,3],[3,1],[3,3],[2,2]],
            4
        ),
        (
            [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]],
            2
        ),
    ]
    test(Solution().minAreaRect, test_data)
