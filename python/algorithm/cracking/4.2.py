# -*- coding:utf-8 -*-
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque

class Path:
    def checkPath(self, a, b):
        # write code here
        return self.traverse(a, b) or self.traverse(b, a)

    def traverse(self, a, b):
        if not (a and b):
            return False
        if a == b:
            return True
        q = deque([a])
        visited = set()
        while q:
            c = q.pop() # curent vertex
            visited.add(c)
            for n in c.neighbors:
                if n == b:
                    return True
                if n not in visited:
                    q.append(n)
        return False

