# -*- coding:utf-8 -*-
class Finder:
    def findMissing(self, numbers, n):
        # write code here
        for i in range(n):
            if i % 2 != numbers[i][0]:
                return i
        return n


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [[0],[0,1]],
                2
            ),
            1
        )
    ]
    test(Finder().findMissing, test_data)
