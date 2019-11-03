# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import List
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        rst = []
        stack = []
        p = head
        i = 0
        while p:
            while stack and p.val > stack[-1][1]:
                rst[stack.pop()[0]] = p.val
            stack.append((len(rst), p.val))
            p = p.next
            rst.append(0)
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [  
        (
            ListNode.create([2,1,5]),
            [5,5,0]
        ),
        (
            ListNode.create([2,7,4,3,5]),
            [7,0,5,5,0]
        ),
        (
            ListNode.create([1,7,5,1,9,2,5,1]),
            [7,9,9,9,0,5,0,0]
        ),
    ]
    test(Solution().nextLargerNodes, test_data)

