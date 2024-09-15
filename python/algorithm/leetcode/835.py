from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        r = 0
        if len(img1) == 0 or len(img2) == 0:
            return 0
        # move the right bottom corner of img1 from (0, 0) to (R1+R2-2, C1+C2-2)
        R1 = len(img1)
        R2 = len(img2)
        C1 = len(img1[0])
        C2 = len(img2[0])

        for i in range(R1+R2-1):
            if i < R2:
                a = R1 - 1
                c = i
            else:
                a = R1 - (i - R2) - 2
                c = R2 - 1
            for j in range(C1+C2-1):
                if j < C2:
                    b = C1 - 1
                    d = j
                else:
                    b = C1 - (j - C2) - 2
                    d = C2 - 1
                r = max(r, self.overlap(img1, img2, a, b, c, d))
        return r

    def overlap(self, img1, img2, a, b, c, d):
        '''
        (a, b) is the index of right bottom corner of the overlap area in img1
        (c, d) ... in img2
        '''
        if (a, b, c, d) == (4, 0, 0, 4):
            import pdb
            pdb.set_trace()
        r = 0
        i1, i2 = a, c
        while i1 >= 0 and i2 >= 0:
            j1, j2 = b, d # important
            while j1 >= 0 and j2 >= 0:
                if img1[i1][j1] == 1 and img2[i2][j2] == 1:
                    r += 1
                j1 -= 1
                j2 -= 1
            i1 -= 1
            i2 -= 1
        return r

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [[1,1,0],[0,1,0],[0,1,0]],
                [[0,0,0],[0,1,1],[0,0,1]]
            ),
            3
        ),
        (
            (
                [[1]],
                [[1]]
            ),
            1
        ),
        (
            (
                [[0]],
                [[0]]
            ),
            0
        ),
        (
            (
                [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]
            ),
            1
        )
    ]
    test(Solution().largestOverlap, test_data)

