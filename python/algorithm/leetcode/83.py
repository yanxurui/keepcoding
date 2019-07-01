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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ans = None
        p = None
        c = head
        while c:
            n = 0
            while c.next and c.next.val == c.val:
                c = c.next
                n += 1
            if p is None:
                p = c
                ans = p
            else:
                p.next = c
                p = c
            c = c.next
        if p:
            p.next = None
        return ans


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ListNode.create([1,1,2]),
            ListNode.create([1,2])
        ),
        (
            ListNode.create([1,1,2,3,3]),
            ListNode.create([1,2,3])
        ),
        (
            ListNode.create([1,2,2]),
            ListNode.create([1,2])
        ),
        (
            ListNode.create([1,1]),
            ListNode.create([1])
        )
        
    ]
    test(Solution().deleteDuplicates, test_data)
