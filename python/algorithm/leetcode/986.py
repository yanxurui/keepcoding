# https://leetcode.com/problems/interval-list-intersections/discuss/231108/C%2B%2B-O(n)-%22merge-sort%22
from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rst = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][0] > B[j][1]:
                j += 1
            else:
                rst.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] < B[j][1]:
                    i+= 1
                else:
                    j += 1
        return rst
        

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [[0,2],[5,10],[13,23],[24,25]],
                [[1,5],[8,12],[15,24],[25,26]]
            ),
            [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        )
    ]
    test(Solution().intervalIntersection, test_data)

