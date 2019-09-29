# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        tmp = []
        p = listNode
        while p:
            tmp.append(p.val)
            p = p.next
        return tmp[::-1]


# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (ListNode.create([1,2,3])),
            [3,2,1]
        )
    ]
    test(Solution().printListFromTailToHead, test_data)
