# -*- coding:utf-8 -*-
class BinInsert:
    def binInsert(self, n, m, j, i):
        # write code here
        return n | (m << j)

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode, TreeNode
    test_data = [
        (
            (1024, 19, 2, 6),
            1100
        )
    ]
    test(BinInsert().binInsert, test_data)
