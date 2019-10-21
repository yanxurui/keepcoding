# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        rst = p = ListNode(0)
        r = 0
        while l1 and l2:
            s = l1.val + l2.val + r # sum
            r = s // 10
            v = s % 10
            p.next = ListNode(v)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 else l2
        while l:
            s = l.val + r
            r = s // 10
            v = s % 10
            p.next = ListNode(v)
            p = p.next
            l = l.next
        if r > 0 or rst == p:
            p.next = ListNode(r)
        return rst.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode

    test_data = [  
        (
            (
                ListNode.create([2, 4, 3]),
                ListNode.create([5, 6, 4]),  
            ),
            ListNode.create([7, 0, 8]),  
        ),
        (
            (
                ListNode.create([0]),
                ListNode.create([0]),  
            ),
            ListNode.create([0]),  
        )
    ]
    test(Solution().addTwoNumbers, test_data)

