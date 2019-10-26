# -*- coding:utf-8 -*-

class UnusualAdd:
    def addAB(self, A, B):
        # write code here
        while B:
            x = A^B # xor
            a = A&B # and
            A = x
            B = a<<1
        return A


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            (1,2),
            3
        ),
        
    ]
    test(UnusualAdd().addAB, test_data)
