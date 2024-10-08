# https://leetcode.com/problems/reverse-linked-list/discuss/58125/In-place-iterative-and-recursive-Java-solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # return self.reverseListInt(head, None)
        return self.reverseListIte3(head)

    def reverseListRec(self, head, tail):
        if not head:
            return tail
        newHead = head.next
        head.next = tail
        return self.reverseListRec(newHead, head)

    def reverseListIte(self, head):
        tail = None
        while head:
            newHead = head.next
            head.next = tail
            tail = head
            head = newHead
        return tail

    def reverseListIte2(self, head):
        ans = None
        while head:
            newHead = head.next
            head.next = ans
            ans = head
            head = newHead
        return ans

    def reverseListIte3(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ListNode.create([1,2,3,4,5]),
            ListNode.create([5,4,3,2,1]),
        )
    ]
    test(Solution().reverseList, test_data)
