# https://leetcode.com/problems/remove-boxes/discuss/101310/Java-top-down-and-bottom-up-DP-solutions
from collections import defaultdict

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        tab = defaultdict(int)

        def removeBoxesSub(i, j, k):
            if i>j:
                return 0
            if tab[(i,j,k)] > 0:
                return tab[(i,j,k)]
            # optimization to avoid TLE
            while i < j and boxes[i+1] == boxes[i]:
                i += 1
                k += 1
            res = (k+1)**2 + removeBoxesSub(i+1, j, 0)
            for m in range(i+1, j+1):
                if boxes[i] == boxes[m]:
                    # attach i to m
                    res = max(res, removeBoxesSub(i+1, m-1, 0)+removeBoxesSub(m, j, k+1))
            tab[(i,j,k)] = res # cache for future look up
            return res

        return removeBoxesSub(0, len(boxes)-1, 0)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [1, 3, 2, 2, 2, 3, 4, 3, 1],
            23
        )
    ]
    test(Solution().removeBoxes, test_data)

