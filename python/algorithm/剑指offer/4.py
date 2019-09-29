# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        val = pre[0]
        root = TreeNode(val)
        idx = tin.index(val)
        if idx > 0:
            root.left = self.reConstructBinaryTree(pre[1:idx+1], tin[:idx])
        else:
            root.left = None
        if idx < len(tin)-1:
            root.right = self.reConstructBinaryTree(pre[idx+1:], tin[idx+1:])
        else:
            root.right = None
        return root



# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (
                [1,2,4,7,3,5,6,8],
                [4,7,2,1,5,3,8,6]
            ),
            TreeNode.create([1, 2,3, 4,None, 5,6, None,7, None,None, 8,None])
        )
    ]
    test(Solution().reConstructBinaryTree, test_data)
