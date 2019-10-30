"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        self.sub(head)
        return head

    def sub(self, p):
        '''return the tail
        '''
        assert p
        while p:
            if p.child:
                h, t = p.child, self.sub(p.child)
                p.child = None
                # insert after p
                t.next = p.next
                if t.next:
                    t.next.prev = t
                h.prev = p
                p.next = h
                p = t.next
            else:
                t = p
                p = p.next
        return t




if __name__ == '__main__':
    from testfunc import test
