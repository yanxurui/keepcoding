# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Checker:
    def checkBST(self, root):
        # write code here
        return self.util(root)

    def util(self, root, upper=None, lower=None):
        if root:
            if upper and root.val >= upper:
                return False
            if lower and root.val <= lower:
                return False
            if not self.util(root.left, upper=min(upper, root.val) if upper else root.val, lower=lower):
                return False
            if not self.util(root.right, upper=upper, lower=max(lower, root.val) if lower else root.val):
                return False
        return True



if __name__ == '__main__':
    from testfunc import test
    from common import ListNode, TreeNode
    test_data = [
        (
            TreeNode.create([1,2,3,4,5,6]),
            False,
        ),
        (
            TreeNode.create([3,1,5,None,2,4,6]),
            True,
        ),
        (
            TreeNode.create([1]),
            True,
        ),

    ]
    test(Checker().checkBST, test_data)
