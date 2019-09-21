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
        if head is None or head.next is None:
            return
        # 1. find the middle of the list
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        # print(p1)
        # 2. reverse the second half
        pre_middle = p1
        pre_current = pre_middle.next
        while pre_current.next:
            current = pre_current.next
            pre_current.next = current.next
            current.next = pre_middle.next
            pre_middle.next = current
        # print(head)
        # 3. reorder
        p1 = head
        p2 = pre_middle.next
        while p1 != pre_middle:
            pre_middle.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pre_middle.next
        # print(head)


def wrapper(head):
    Solution().reorderList(head)
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
    test(wrapper, test_data)

