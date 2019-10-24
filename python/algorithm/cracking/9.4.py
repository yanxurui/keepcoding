# -*- coding:utf-8 -*-
class Subset:
    # 返回二维[[],[],[]]
    def getSubsets(self, A, n):
        # write code here
        rst = [[]]
        for i in A:
            j = len(rst)
            for k in range(j):
                l = rst[k]
                rst.append(l+[i])
        rst.pop(0)
        for l in rst:
            l.sort(key=lambda v: -v)
        rst.sort()
        rst = rst[::-1]
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [123,456,789],
                3
            ),
            [[789,456,123],[789,456],[789,123],[789],[456,123],[456],[123]]
        )
    ]
    test(Subset().getSubsets, test_data)
