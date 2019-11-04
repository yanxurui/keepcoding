from typing import List
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        j = None
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                k = i+1
                for j in range(i+1, len(A)):
                    # find the maximum value that is smaller than A[i], if there is a tie, get the closest one
                    if A[j] < A[i]:
                        if A[j] > A[k]: # to avoid tie
                            k = j
                    else:
                        break
                A[i], A[k] = A[k], A[i]
                break
        return A


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [3,2,1],
            [3,1,2]
        ),
        (
            [1,1,5],
            [1,1,5]
        ),
        (
            [1,9,4,6,7],
            [1,7,4,6,9]
        ),
        (
            [3,1,1,3],
            [1,3,1,3]
        ),
    ]
    test(Solution().prevPermOpt1, test_data)

