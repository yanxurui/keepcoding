# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        rst = head
        prev = None
        remaining = head
        while remaining:
            slow = fast = remaining
            i = 0
            while i < k-1 and fast.next:
                fast = fast.next
                i += 1
            if i < k-1:
                if prev:
                    prev.next = remaining
                break
            remaining = fast.next
            fast.next = None
            r = self.reverse(slow)
            if prev:
                prev.next = r
            else:
                rst = r
            prev = slow
        return rst

    def reverse(self, head):
        prev = None
        p = head
        while p:
            r = p.next
            p.next = prev
            prev = p
            p = r
        return prev


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                ListNode.create([1, 2, 3, 4, 5]),
                2
            ),
            ListNode.create([2, 1, 4, 3, 5])
        ),
        (
            (
                ListNode.create([1, 2, 3, 4, 5]),
                3
            ),
            ListNode.create([3, 2, 1, 4, 5])
        ),
        
    ]
    test(Solution().reverseKGroup, test_data)
