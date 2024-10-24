# https://leetcode.com/problems/sort-list/discuss/46714/Java-merge-sort-solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # 1. split into 2 sublists
        prev = None
        slow, fast = head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        # 2. merge sort
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        l = ListNode(0)
        p = l
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
        return l.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (ListNode.create([4,2,1,3])),
            ListNode.create([1,2,3,4])
        ),
        (
            (ListNode.create([-1,5,3,4,0])),
            ListNode.create([-1,0,3,4,5])
        ),
        (
            (ListNode.create([1])),
            ListNode.create([1])
        )
    ]
    test(Solution().sortList, test_data)

