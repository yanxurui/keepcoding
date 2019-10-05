# https://leetcode.com/problems/palindrome-linked-list/discuss/64501/Java-easy-to-understand

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast: # odd number, skip the middle one
            slow = slow.next
        slow = self.reverse(slow)
        while slow:
            if head.val != slow.val:
                return False                
            head = head.next
            slow = slow.next
        return True

    def reverse(self, head):
        prev = None
        while head:
            n = head.next
            head.next = prev
            prev = head
            head = n
        return prev


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (ListNode.create([1,2])),
            False
        ),
        (
            (ListNode.create([1,2,2,1])),
            True
        ),
        (
            (ListNode.create([1,2,1])),
            True
        ),
        (
            (ListNode.create([1,1])),
            True
        ),
        (
            (ListNode.create([1])),
            True
        )
    ]
    test(Solution().isPalindrome, test_data)
