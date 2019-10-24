# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode

    test_data = [  
        (
            (
                ListNode.create([1, 2, 4]),
                ListNode.create([1, 3, 4]),  
            ),
            ListNode.create([1, 1, 2, 3, 4, 4]),  
        )
    ]
    test(Solution().mergeTwoLists, test_data)

