# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        H = ListNode(0)
        p = H
        p.next = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return H.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (ListNode.create([1, 2, 6, 3, 4, 5, 6]), 6),
            ListNode.create([1, 2, 3, 4, 5])
        )
    ]
    test(Solution().removeElements, test_data)
