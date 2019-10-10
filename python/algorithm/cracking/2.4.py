# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Partition:
    def partition(self, pHead, x):
        # write code here
        smallHead = small = ListNode(0)
        bigHead = big = ListNode(0)
        p = pHead
        while p:
            if p.val < x:
                small.next = p
                small = small.next
            else:
                big.next = p
                big = big.next
            p = p.next
        big.next = None
        small.next = bigHead.next
        return smallHead.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                ListNode.create([1,6,3,5,2,7]),
                4
            ),
            ListNode.create([1,3,2,6,5,7]),
        )
    ]
    test(Partition().partition, test_data)
