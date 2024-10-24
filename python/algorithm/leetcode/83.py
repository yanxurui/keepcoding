from common import ListNode

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

class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p:
            if p.next and p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


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
        ),
        (
            ListNode.create([1,1,1]),
            ListNode.create([1])
        ),
        
    ]
    test(Solution2().deleteDuplicates, test_data)
