# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeLevel:
    def getTreeLevel(self, root, dep):
        # write code here
        level = 1
        q = [root]
        while level < dep:
            newQ = []
            for n in q:
                if n:
                    if n.left:
                        newQ.append(n.left)
                    if n.right:
                        newQ.append(n.right)
            q = newQ
            level += 1
        head = tail = ListNode(0)
        for n in q:
            tail.next = ListNode(n.val)
            tail = tail.next
        return head.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode, TreeNode
    test_data = [
        (
            (
                TreeNode.create([1,2,3,4,5,6]),
                2
            ),
            ListNode.create([2, 3])
        ),

    ]
    test(TreeLevel().getTreeLevel, test_data)
