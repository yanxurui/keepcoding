# https://leetcode.com/problems/reorder-list/discuss/44992/Java-solution-with-3-steps

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from common import ListNode

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        
        # 1. find the middle of the list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse the second half (nodes after slow)
        p = slow.next
        slow.next = None
        while p:
            tmp = p.next
            p.next = slow.next
            slow.next = p
            p = tmp

        # 3. alternate
        p1 = head
        p2 = slow.next
        while p1 and p2:
            slow.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = slow.next
        return head


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (ListNode.create([1,2,3,4])),
            ListNode.create([1,4,2,3])
        ),
        (
            (ListNode.create([1,2,3,4,5])),
            ListNode.create([1,5,2,4,3])
        ),
        (
            (ListNode.create([1])),
            ListNode.create([1])
        ),
        (
            (ListNode.create([1,2,3,4,5,6,7])),
            ListNode.create([1,7,2,6,3,5,4])
        ),
    ]
    test(Solution().reorderList, test_data)

