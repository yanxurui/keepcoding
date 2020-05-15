class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p, q = head, None
        k1, k2, k3, k4 = (None,)*4
        i = 1
        while p:
            if i == m - 1:
                k1 = p
            if i == m:
                k2 = p
            tmp = p
            p = p.next
            if k2:
                tmp.next = q
            q = tmp
            if i == n:
                k3 = tmp
                k4 = p
                if k1:
                    k1.next = k3
                else:
                    head = k3
                k2.next = k4
                break
            i += 1
        return head


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
    test(Solution().reverseBetween, test_data)
