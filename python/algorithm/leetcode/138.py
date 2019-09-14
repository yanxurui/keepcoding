"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

"""
Input:
{
    "$id":"1",
    "next":{
        "$id":"2",
        "next":null,
        "random":{"$ref":"2"},
        "val":2},
    "random":{"$ref":"2"},
    "val":1
}
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.d = {}
        return self.clone(head)

    def clone(self, head):
        if head is None:
            return None
        N = self.d.get(head, None)
        if N is None:
            N = Node(head.val, None, None)
            self.d[head] = N
            N.next = self.clone(head.next)
            N.random = self.clone(head.random)
        return N


