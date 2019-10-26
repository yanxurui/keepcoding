# -*- coding:utf-8 -*-

class Frequency:
    def getFrequency(self, article, n, word):
        # write code here
        rst = 0
        for w in article:
            if w == word:
                rst += 1
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                ['a','ab'], 2,
                'a'
            ),
            1
        )
    ]
    test(Frequency().getFrequency, test_data)
