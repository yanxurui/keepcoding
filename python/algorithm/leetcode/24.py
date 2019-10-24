# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        rst = prev = None
        remaining = head
        while remaining:
            slow = fast = remaining
            remaining = None
            for i in range(2-1):
                if not fast.next:
                    break
                fast = fast.next
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
            ListNode.create([1, 2, 3, 4]),
            ListNode.create([2, 1, 4, 3])
        ),
        (
            ListNode.create([1]),
            ListNode.create([1])
        ),
    ]
    test(Solution().swapPairs, test_data)
