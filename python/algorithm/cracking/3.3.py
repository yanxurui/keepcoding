# -*- coding:utf-8 -*-
class SetOfStacks:
    def setOfStacks(self, ope, size):
        # write code here
        rst = [[]]
        cur = 0
        for op, val in ope:
            if op == 1:
                if len(rst[cur]) >= size:
                    rst.append([])
                    cur += 1
                rst[cur].append(val)
            elif op == 2:
                rst[cur].pop()
                if len(rst[cur]) == 0:
                    cur -= 1
                    rst.pop()
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                [
                    [1, 1],
                    [2, 0],
                ],
                2
            ),
            [
            ]
        ),
        (
            (
                [
                    [1, 1],
                    [1, 1],
                    [1, 1],
                    [2, 0],
                ],
                2
            ),
            [
                [1,1]
            ]
        ),
        (
            (
                [
                    [1, 1],
                    [1, 1],
                    [1, 1],
                    [1, 1],
                    [1, 1],
                    [2, 0],
                    [2, 0],
                ],
                2
            ),
            [
                [1,1],
                [1],
            ]
        ),
        
    ]
    test(SetOfStacks().setOfStacks, test_data)
