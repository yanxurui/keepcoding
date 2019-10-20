# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        rst = []
        self.traverse(root, 0, expectNumber, [], rst)
        rst = sorted(rst, key=lambda l:-len(l))
        return rst

    def traverse(self, root, s, t, path, rst):
        if not root:
            return
        s += root.val
        path = path+[root.val]
        if not (root.left or root.right):
            # leaf node
            if s == t:
                rst.append(path)
        else:
            self.traverse(root.left, s, t, path, rst)
            self.traverse(root.right, s, t, path, rst)


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode, TreeNode
    test_data = [
        (
            (
                TreeNode.create([1,2,4,3,2]),
                5
            ),
            [[1,2,2],[1,4]]
        ),
        (
            (
                TreeNode.create([5,4,None,3,None,2,None,1]),
                15
            ),
            [[5,4,3,2,1]]
        ),
    ]
    test(Solution().FindPath, test_data)
