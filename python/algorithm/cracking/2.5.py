class Plus:
    def plusAB(self, a, b):
        # write code here
        rst = ListNode(0)
        p = rst
        r = 0
        while a and b:
            s = a.val + b.val + r
            r = s//10
            p.next = ListNode(s%10)
            p = p.next
            a = a.next
            b = b.next
        c = a or b
        while c:
            s = c.val + r
            r = s//10
            p.next = ListNode(s%10)
            p = p.next
            c = c.next
        if r:
            p.next = ListNode(r)
        return rst.next


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                ListNode.create([1,2,3]),
                ListNode.create([3,2,1]),
            ),
            ListNode.create([4,4,4]),
        ),
        (
            (
                ListNode.create([1,2,3]),
                ListNode.create([2,8,1]),
            ),
            ListNode.create([3,0,5]),
        ),
        (
            (
                ListNode.create([1]),
                ListNode.create([9,9,9]),
            ),
            ListNode.create([0,0,0,1]),
        )
    ]
    test(Plus().plusAB, test_data)
