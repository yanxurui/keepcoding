# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Remove:
    def removeNode(self, pNode):
        # write code here
        if not (pNode and pNode.next):
            return False
        while pNode.next:
            pNode.val = pNode.next.val
            prev = pNode
            pNode = pNode.next
        prev.next = None
        return True


if __name__ == '__main__':
    from testfunc import test
