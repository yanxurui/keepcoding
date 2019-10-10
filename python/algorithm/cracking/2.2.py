# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        p = q = head
        for i in range(k):
            if not p:
                return None
            p = p.next
        while p:
            p = p.next
            q = q.next
        return q

if __name__ == '__main__':
    from testfunc import test
