# -*- coding:utf-8 -*-
class LCA:
    def getLCA(self, a, b):
        # write code here
        path_a = self.path(a)
        path_b = self.path(b)
        for i, (p1,p2) in enumerate(zip(path_a, path_b)):
            if p1 != p2:
                break
        return path_a[i-1]

    def path(self, v):
        rst = []
        while v:
            rst.append(v)
            v = v//2
        return rst[::-1]


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode, TreeNode
    test_data = [
        (
            (2,3),
            1
        ),
        (
            (5, 6),
            1
        ),
        (
            (9, 8),
            4
        ),
        (
            (9, 7),
            1
        ),

    ]
    test(LCA().getLCA, test_data)
