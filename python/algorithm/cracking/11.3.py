# -*- coding:utf-8 -*-

class Finder:
    def findElement(self, A, n, x):
        # write code here
        l = 0
        h = n-1
        while l <= h:
            m = (l+h)//2
            if A[m] == x:
                return m
            if A[m] >= A[l]:
                if x > A[m]:
                    l = m+1
                else:
                    if x < A[l]:
                        l = m+1
                    else:
                        h = m-1
            else:
                if x > A[m]:
                    if x < A[l]:
                        l = m+1
                    else:
                        h = m-1
                else:
                    h = m-1
        return -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [6,1,2,3,4,5],6,6
            ),
            0
        ),
        (
            (
                [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,1,2,3,4,5,6,7,8,9],80,6
            ),
            76
        ),
    ]
    test(Finder().findElement, test_data)
