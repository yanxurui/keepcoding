class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        return self.dfs(0, target, startFuel, stations, 0)

    def dfs(self, start, target, startFuel, stations, stops):
        if not stations:
            if startFuel < (target - start):
                return -1
            else:
                return stops
        else:
            if startFuel < stations[0][0] - start:
                return -1
            else:
                # no refuel
                a = self.dfs(stations[0][0], target, startFuel-(stations[0][0]-start), stations[1:], stops)
                # refuel
                b = self.dfs(stations[0][0], target, startFuel-(stations[0][0]-start)+stations[0][1], stations[1:], stops+1)
                if a == -1 or b == -1:
                    return max(a, b)
                else:
                    return min(a, b)

        

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
            0
        )
    ]
    test(Solution().minRefuelStops, test_data)
