# https://leetcode.com/problems/linked-list-cycle/discuss/44489/O(1)-Space-Solution

from common import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        walker = head
        runner = head
        while walker and runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker is runner:
                return True
        return False


if __name__ == '__main__':
    from testfunc import test
    def create(vals, pos):
        head = ListNode.create([3,2,0,-4])
        if pos == -1:
            return head
        p = head
        i = 0
        while True:
            if i == pos:
                tail = p
            if p.next is None:
                break
            else:
                i += 1
                p = p.next
        p.next = tail
        return head

    test_data = [  
        (
            (create([3,2,0,-4], 1)),
            True
        ),
        (
            (create([1, 2], 0)),
            True
        ),
        (
            (create([1], -1)),
            False
        ),
    ]
    test(Solution().hasCycle, test_data)
