# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        walker = runner = head
        while runner and runner.next:
            runner = runner.next.next
            walker = walker.next
        return walker # no matter odd or even


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    ll1 = ListNode.create([1,2,3,4,5])
    ll2 = ListNode.create([1,2,3,4,5,6])
    test_data = [  
        (
            ll1,
            ll1.next.next
        ),
        (
            ll2,
            ll2.next.next.next
        ),
    ]
    test(Solution().middleNode, test_data)

