"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque([root, None])
        rst = []
        level = []
        while q:
            n = q.popleft()
            if n:
                level.append(n.val)
                for c in n.children:
                    if c:
                        q.append(c)
            else:
                if level:
                    rst.append(level)
                    level = []
                    q.append(None) # sep
                else:
                    break
        return rst
