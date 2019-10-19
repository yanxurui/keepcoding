# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def abs(a, b):
    if a > b:
        return abs(b, a)
    return b - a

class Balance:
    def isBalance(self, root):
        # write code here
        _, balance = self.height(root)
        return balance

    def height(self, root):
        if not root:
            return 0, True
        l, b1 = self.height(root.left)
        r, b2 = self.height(root.right)
        balance = False
        if b1 and b2 and abs(l, r) <= 1:
            balance = True
        return 1 + max(l, r), balance


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (TreeNode.create([1,2,3,4,None,None,None])),
            True
        )
    ]
    test(Balance().isBalance, test_data)

