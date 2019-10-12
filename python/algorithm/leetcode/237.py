# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        while True:
            p.val = p.next.val
            if not p.next.next:
                # arrive at the second last node
                p.next = None
                break
            p = p.next

def wrapper(head, node):
    Solution().deleteNode(node)
    return head


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    head = ListNode.create([4,5,1,9])
    test_data = [
        (
            (
                head,
                head.next
            ),
            ListNode.create([4,1,9])
        )
    ]
    test(wrapper, test_data)
