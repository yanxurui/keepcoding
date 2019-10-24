# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        i = 0
        while i < n:
            if A[i] == i:
                return True
            elif A[i] < i:
                i += 1
            else:
                if A[i] < n:
                    i = A[i]
                else:
                    break
        return False
                



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,1,3,4,5],
                5
            ),
            True
        ),
        (
            (
                [0,0,1,2,4],
                5
            ),
            True
        ),
    ]
    test(MagicIndex().findMagicIndex, test_data)
