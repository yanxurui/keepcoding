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
class Converter:
    def treeToList(self, root):
        # write code here
        head, _ = self.sub(root)
        return head

    def sub(self, root):
        if root:
            cur = ListNode(root.val)
            head, tail = self.sub(root.left)
            if head:
                assert tail
                tail.next = cur
            else:
                # left child is empty
                head = cur
            head2, tail = self.sub(root.right)
            if head2:
                cur.next = head2
            else:
                # right child is empty
                tail = cur
            return head, tail
        else:
            return None, None


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            TreeNode.create([3,1,5,None,2,4]),
            ListNode.create([1,2,3,4,5])
        ),
        
    ]
    test(Converter().treeToList, test_data)
