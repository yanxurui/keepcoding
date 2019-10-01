class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        buildings_merged = [] # no overlap
        buildings_by_height = sorted(buildings, key=lambda item: item[2])
        while buildings_by_height:
            b = buildings_by_height.pop()
            for taller in buildings_merged:
                if taller[0] > b[0] and taller[0] < b[1] and taller[1] >= b[1]:
                    # left side of taller building is inside current building
                    b = (b[0], taller[0], b[2])
                elif taller[1] > b[0] and taller[1] < b[1] and taller[0] <= b[0]:
                    # right
                    b = (taller[1], b[1], b[2])
                elif taller[1] < b[1] and taller[0] > b[0]:
                    # both sides
                    # split into 2
                    buildings_by_height.append((taller[1], b[1], b[2]))
                    b = (b[0], taller[0], b[2])
                elif taller[0] <= b[0] and taller[1] >= b[1]:
                    # ignored
                    b = None
                    break
                else:
                    continue
            if b:
                buildings_merged.append(b)
        if not buildings_merged:
            return []
        buildings_merged = sorted(buildings_merged, key=lambda item: item[0])
        res = [[buildings_merged[0][0], buildings_merged[0][2]]]
        for i in range(1, len(buildings_merged)):
            if buildings_merged[i][0] != buildings_merged[i-1][1]:
                # interval
                res.append([buildings_merged[i-1][1], 0])
            if buildings_merged[i][2] != res[-1][1]:
                # merge same height
                res.append([buildings_merged[i][0], buildings_merged[i][2]])
        res.append([buildings_merged[-1][1], 0])
        return res


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [
        (
            ([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]),
            [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ]
        ),
        (
            ([[1,2,1],[1,2,2],[1,2,3]]),
            [[1,3],[2,0]]
        ),
        (
            ([[0,2,3],[2,4,3],[4,6,3]]),
            [[0,3], [6,0]]
        ),
        (
            ([[0,3,3],[1,5,3],[2,4,3],[3,7,3]]),
            [[0,3], [7,0]]
        ),
        (
            ([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]),
            [[2,70],[4,30],[6,41],[7,70],[10,102],[30,41],[60,91],[80,72],[90,59],[120,0]]
        )
    ]
    test(Solution().getSkyline, test_data)
