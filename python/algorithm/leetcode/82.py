
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
            if n == 0:
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
            ListNode.create([1,2,3,3,4,4,5]),
            ListNode.create([1,2,5])
        ),
        (
            ListNode.create([1,1,1,2,3]),
            ListNode.create([2,3])
        ),
        (
            ListNode.create([1,2,2]),
            ListNode.create([1])
        ),
        (
            ListNode.create([1,1]),
            ListNode.create([])
        )
        
    ]
    test(Solution().deleteDuplicates, test_data)
