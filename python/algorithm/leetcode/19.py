# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            # total length is n
            return slow.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [  
        (
            (
                ListNode.create([1,2,3,4,5]),
                2
            ),
            ListNode.create([1,2,3,5]),
        ),
        (
            (
                ListNode.create([1]),
                1
            ),
            ListNode.create([]),
        ),
        (
            (
                ListNode.create([1,2]),
                2
            ),
            ListNode.create([2]),
        )
    ]
    test(Solution().removeNthFromEnd, test_data)

