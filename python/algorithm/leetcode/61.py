# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create(cls, l):
        head, tail = None, None
        for x in l:
            n = cls(x)
            if head is None:
                head = n
            else:
                tail.next = n
            tail = n
        return head
    def __str__(self):
        l = []
        p = self
        while p is not None:
            l.append(p.val)
            p = p.next
        return '->'.join(map(str, l))

    def __eq__(self, other):
        return str(self) == str(other)

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        n = 0
        while p is not None:
            p = p.next
            n += 1
        m = n- k%n -1
        p = head
        for i in range(m):
            p = p.next
        if p.next is None:
            return head

        tmp = head
        head = p.next
        p.next = None
        p = head
        while p.next is not None:
            p = p.next
        p.next = tmp
        return head

        
if __name__ == '__main__':
    from testfunc import test

    test_data = [
        (
            (
                ListNode.create([1,2,3,4,5]),
                2
            ),
            ListNode.create([4,5,1,2,3])
        ),
        (
            (
                ListNode.create([0,1,2]),
                4
            ),
            ListNode.create([2,0,1])
        ),
        (
            (
                ListNode.create([]),
                0
            ),
            ListNode.create([])
        )
    ]
    test(Solution().rotateRight, test_data)
