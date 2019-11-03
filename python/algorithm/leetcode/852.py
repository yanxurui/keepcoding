from typing import List
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A)-1):
            if A[i] > A[i+1]:
                return i

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [0,1,0],
            1
        ),
        (
            [0,2,1,0],
            1
        )
    ]
    test(Solution().peakIndexInMountainArray, test_data)

