# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Palindrome:
    def isPalindrome(self, pHead):
        # write code here
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast: # odd
            slow = slow.next
        p = pHead
        q = self.reverse(slow)
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

    def reverse(self, root):
        p = root
        prev = None
        while p:
            tmp = p.next
            p.next = prev
            prev = p
            p = tmp
        return prev


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            ListNode.create([1,2,3,2,1]),
            True
        ),
        (
            ListNode.create([1,2,2,1]),
            True
        ),
        (
            ListNode.create([1,2,3,1,2]),
            False
        ),
    ]
    test(Palindrome().isPalindrome, test_data)
