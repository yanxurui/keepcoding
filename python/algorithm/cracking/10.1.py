# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

class Joseph:
    def getResult(self, n, m):
        # write code here
        head = p = ListNode(0)
        for i in range(1, n+1):
            p.next = ListNode(i)
            p = p.next
        p.next = head.next
        while p != p.next:
            for j in range(m-1):
                p = p.next
            p.next = p.next.next
        return p.val


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                5,
                3
            ),
            4
        ),
        (
            (
                2,
                3
            ),
            2
        ),
    ]
    test(Joseph().getResult, test_data)
