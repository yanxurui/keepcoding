# https://leetcode.com/problems/minimum-number-of-refueling-stops/discuss/149839/DP-O(N2)-and-Priority-Queue-O(NlogN)

import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        cur = startFuel
        q = []
        rst = 0
        i = 0
        while cur < target:
            while i < len(stations):
                s = stations[i]
                if cur >= s[0]:
                    heapq.heappush(q, -s[1])
                else:
                    break
                i += 1
            if q:
                cur += -heapq.heappop(q)
                rst += 1
            else:
                return -1
        return rst
        

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                1,
                1,
                []
            ),
            0
        ),
        (
            (
                100,
                1,
                [[10,100]]
            ),
            -1
        ),
        (
            (
                100,
                10,
                [[10,60],[20,30],[30,30],[60,40]]
            ),
            2
        ),
        (
            (
                1000,
                1,
                [
                    [1,186],
                    [145,161],
                    [183,43],
                    [235,196],
                    [255,169],
                    [263,200],
                    [353,161],
                    [384,190],
                    [474,44],
                    [486,43],
                    [567,48],
                    [568,96],
                    [592,36],
                    [634,181],
                    [645,167],
                    [646,69],
                    [690,52],
                    [732,28],
                    [800,42],
                    [857,55],
                    [922,63],
                    [960,141],
                    [973,13],
                    [977,112],
                    [997,162]
                ]
            ),
            6
        )
    ]
    test(Solution().minRefuelStops, test_data)
