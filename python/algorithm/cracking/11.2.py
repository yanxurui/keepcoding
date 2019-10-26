# -*- coding:utf-8 -*-
class SortString:
    def sortStrings(self, s, n):
        rst = []
        S = set()
        for w in sorted(s):
            w_s = ''.join(sorted(w))
            if w_s not in S:
                S.add(w_s)
                rst.append(w)
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                ["ab","ba","abc","cba"],
                4
            ),
            ["ab","abc"]
        )
    ]
    test(SortString().sortStrings, test_data)
