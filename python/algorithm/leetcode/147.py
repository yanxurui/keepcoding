# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        tail = head
        while tail.next:
            p = tail.next
            tail.next = p.next
            cur = head
            prev = None
            while prev != tail:
                if cur.val < p.val:
                    if cur == tail:
                        p.next = tail.next
                        tail.next = p
                        tail = p
                        break
                    else:
                        prev = cur
                        cur = cur.next
                else:
                    if prev is None:
                        p.next = head
                        head = p
                    else:
                        prev.next = p
                        p.next = cur
                    break
        return head


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (ListNode.create([4,2,1,3])),
            ListNode.create([1,2,3,4])
        ),
        (
            (ListNode.create([-1,5,3,4,0])),
            ListNode.create([-1,0,3,4,5])
        ),
    ]
    test(Solution().insertionSortList, test_data)

