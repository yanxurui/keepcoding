# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create(cls, vals):
        head = None
        p = None
        for v in vals:
            n = cls(v)
            if head is None:
                head = n
                p = head
            else:
                p.next = n
                p = n
        return head

    def __eq__(p, q):
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return p is None and q is None

    def __str__(p):
        vals = []
        while p is not None:
            vals.append(p.val)
            p = p.next
        return str(vals)


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        beforeHead, afterHead, before, after = None, None, None, None

        p = head
        while p:
            if p.val < x:
                if before:
                    before.next = p
                else:
                    beforeHead = p
                before = p
            else:
                if after:
                    after.next = p
                else:
                    afterHead = p
                after = p
            p = p.next

        if before:
            head = beforeHead
            before.next = afterHead
        else:
            head = afterHead
        if after:
            after.next = None

        return head




if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                (
                    ListNode.create([1,4,3,2,5,2]),
                    3
                ),
                ListNode.create([1,2,2,4,3,5])
            )
        )
    ]
    test(Solution().partition, test_data)
