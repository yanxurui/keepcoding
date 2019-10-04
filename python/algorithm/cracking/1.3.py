# -*- coding:utf-8 -*-
from collections import defaultdict

class Same:
    def checkSam(self, stringA, stringB):
        # write code here
        return self.count(stringA) == self.count(stringB)

    def count(self, s):
        res = defaultdict(int)
        for c in s:
            res[c] += 1
        return res

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                'This is nowcoder',
                'is This nowcoder'
            ),
            True
        ),
        (
            (
                'Here you are',
                'Are you here'
            ),
            False
        )
    ]
    test(Same().checkSam, test_data)
