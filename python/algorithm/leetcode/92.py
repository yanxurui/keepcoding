class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p, q = head, None
        # k1 -> m-1, k2 -> m, k3 -> n, k4 -> n+1
        k1, k2, k3, k4 = (None,)*4
        i = 1
        while p:
            if i == m - 1:
                k1 = p
            if i == m:
                k2 = p
            cur = p
            p = p.next # move to node. Important!
            if k2:
                cur.next = q
            q = cur
            if i == n:
                k3 = cur
                k4 = p
                if k1:
                    k1.next = k3
                else:
                    head = k3
                k2.next = k4
                break
            i += 1
        return head

class Solution2(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        i = 1
        p = head
        while p:
            if i == m - 1:
                beforeLeft = p
            if i == m:
                left = p
            if i == n:
                break
            p = p.next
            i += 1
        if p is None:
            beforeLeft.next = self.reverse(left)            
        else:
            right = p
            afterRight = p.next
            right.next = None
            beforeLeft.next = self.reverse(left)
            left.next = afterRight
        return head

    def reverse(self, head):
        newHead = None
        while head:
            tmp = head.next
            head.next = newHead
            newHead = head
            head = tmp
        return newHead


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [  
        (
            (
                ListNode.create([1,2,3,4,5]),
                2,4
            ),
            ListNode.create([1,4,3,2,5]),
        )
    ]
    test(Solution2().reverseBetween, test_data)
