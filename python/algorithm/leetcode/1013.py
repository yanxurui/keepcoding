from typing import List
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s//3
        find = 0
        s = 0
        for i in range(len(A)):
            s += A[i]
            if s == target:
                find += 1
                if find == 3:
                    return True
                s = 0
        return False


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [0,2,1,-6,6,-7,9,1,2,0,1],
            True
        ),
        (
            [0,2,1,-6,6,7,9,-1,2,0,1],
            False
        ),
        (
            [3,3,6,5,-2,2,5,1,-9,4],
            True
        )
    ]
    test(Solution().canThreePartsEqualSum, test_data)

