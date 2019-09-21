# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything

from common import ListNode

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        walker = head
        runner = head
        k = None
        while walker and runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if walker is runner:
                k = walker
                break
        if k is None:
            return None

        p = k
        r = head
        while not (p is r):
            p = p.next
            r = r.next
        return p


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
    def compare(a, b):
        if a is b:
            return True
        return False

    input1 = create([3,2,0,-4], 1)
    input2 = create([1, 2], 0)
    input3 = create([1], -1)
    test_data = [  
        (
            (input1),
            input1.next
        ),
        (
            (input2),
            input2
        ),
        (
            (input3),
            None
        ),
    ]
    test(Solution().detectCycle, test_data, compare=compare)
