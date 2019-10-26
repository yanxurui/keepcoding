# -*- coding:utf-8 -*-
from collections import defaultdict

class Result:
    def calcResult(self, A, guess):
        # write code here
        set1 = defaultdict(int)
        set2 = defaultdict(int)
        a, b = 0, 0
        for c1,c2 in zip(A, guess):
            if c1==c2:
                a += 1
            else:
                if set2[c1] > 0:
                    b += 1
                    set2[c1] -= 1
                else:
                    set1[c1] += 1
                if set1[c2] > 0:
                    b += 1
                    set1[c2] -= 1
                else:
                    set2[c2] += 1
        return [a, b]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                "RGBY",
                "GGRR"
            ),
            [1, 1]
        )
    ]
    test(Result().calcResult, test_data)
