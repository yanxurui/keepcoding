# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def len(self, head):
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        return n

    def shift(self, head, n):
        p = head
        for i in range(n):
            p = p.next
        return p

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nA = self.len(headA)
        nB = self.len(headB)
        if nA > nB:
            diff = nA - nB
            pA = self.shift(headA, diff)
            pB = headB
        else:
            diff = nB - nA
            pB = self.shift(headB, diff)
            pA = headA
        while pA and pB:
            if pA is pB:
                return pA
            else:
                pA = pA.next
                pB = pB.next
        return None
        

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    def shift(head, n):
        p = head
        for i in range(n):
            p = p.next
        return p
    A = ListNode.create([4,1,8,4,5])
    res = shift(A, 2)
    B = ListNode.create([5,0,1])
    shift(B, 2).next = res
    
    A2 = ListNode.create([0,9,1,2,4])
    res2 = shift(A2, 3)
    B2 = ListNode.create([3])
    B2.next = res2
    
    test_data = [
        (
            (A, B),
            res
        ),
        (
            (A2, B2),
            res2
        )
    ]
    test(Solution().getIntersectionNode, test_data)
