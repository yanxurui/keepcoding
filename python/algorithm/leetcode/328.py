# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode):
        if not head:
            return head
        odd = head
        evenHead = even = head.next
        while even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
                even.next = odd.next
                even = even.next
            else:
                break
        odd.next = evenHead
        return head


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ListNode.create([1, 2, 3, 4, 5]),
            ListNode.create([1, 3, 5, 2, 4])
        ),
        (
            ListNode.create([2, 1, 3, 5, 6, 4, 7]),
            ListNode.create([2, 3, 6, 7, 1, 5, 4])
        ),
        (
            ListNode.create([1,2,3,4,5,6,7,8]),
            ListNode.create([1,3,5,7,2,4,6,8])
        )
    ]
    test(Solution().oddEvenList, test_data)
