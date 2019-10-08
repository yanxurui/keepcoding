# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Node(object):
    def __init__(self, l):
        self.l = l
        self.val = l.val

    def __lt__(self, other):
        return self.val < other.val


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []
        for l in lists:
            if l:
                heapq.heappush(q, Node(l))
        
        head = p = ListNode(0)
        while q:
            l = heapq.heappop(q).l
            if l.next:
                heapq.heappush(q, Node(l.next))
            p.next = l
            p = l
        return head.next
        

if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                [
                  ListNode.create([1,4,5]),
                  ListNode.create([1,3,4]),
                  ListNode.create([2,6])
                ]
            ),
            ListNode.create([1,1,2,3,4,4,5,6])
        ),
        (
            ([None]),
            None
        ),
    ]
    test(Solution().mergeKLists, test_data)
