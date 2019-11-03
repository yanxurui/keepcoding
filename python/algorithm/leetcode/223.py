class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (C-A) * (D-B) + (G-E) * (H-F) - self.interset(A,C, E,G)*self.interset(B,D, F,H)

    def interset(self, a1,a2, b1,b2):
        # return the intersection of two line segment (a1, a2), (b1, b2)
        # if a1 >= b1 and a1 <= b2:
        #     return min(a2, b2) - a1
        # if a2 >= b1 and a2 <= b2:
        #     return a2 - max(a1, b1)
        # if a1 < b1 and a2 > b2:
        #     return b2 - b1
        # return 0
        return max(0, min(a2, b2) - max(a1, b1))

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                -3, 0, 3, 4,
                0, -1, 9, 2
            ),
            45
        ),
        (
            (
                -2, -2, 2, 2,
                -1, -1, 1, 1
            ),
            16
        ),
    ]
    test(Solution().computeArea, test_data)
    test(Solution().interset, [((1,3,2,4),1)])
