# https://leetcode.com/problems/max-points-on-a-line/discuss/47113/A-java-solution-with-notes

from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        res = 0
        for i in range(len(points)):
            x1, y1 = points[i]
            m = 0
            overlap = 0
            d = defaultdict(int)
            for j in range(i):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                gcd = self.gen_gcd(dx, dy)
                if gcd != 0:
                    dx /= gcd
                    dy /= gcd
                ind = (dx, dy)
                d[ind] += 1
                m = max(m, d[ind])
            res = max(res, m + overlap + 1)
        return res


    def gen_gcd(self, a, b):
        if b == 0:
            return a
        return self.gen_gcd(b, a%b)


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ([[1,1],[2,2],[3,3]]),
            3
        ),
        (
            ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]),
            4
        ),
        (
            ([[0,0]]),
            1
        ),
        (
            ([[0,0],[1,1],[0,0]]),
            3
        )
    ]
    test(Solution().maxPoints, test_data)

