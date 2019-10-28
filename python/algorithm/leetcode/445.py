# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        while l1:
            num1 = 10*num1 + l1.val
            l1 = l1.next
        num2 = 0
        while l2:
            num2 = 10*num2 + l2.val
            l2 = l2.next
        s = num1 + num2
        head = ListNode(0)
        if s == 0:
            return head
        while s:
            r = s%10
            node = ListNode(r)
            node.next = head.next
            head.next = node
            s = s//10
        return head.next
            


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode

    test_data = [  
        (
            (
                ListNode.create([7, 2, 4, 3]),
                ListNode.create([5, 6, 4])
            ),
            ListNode.create([7, 8, 0, 7])
        ),
        (
            (
                ListNode.create([0]),
                ListNode.create([0])
            ),
            ListNode.create([0])
        ),
    ]
    test(Solution().addTwoNumbers, test_data)

