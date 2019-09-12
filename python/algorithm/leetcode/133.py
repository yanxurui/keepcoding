"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        return self.dfs(node, {})

    def dfs(self, node, d):
        if node in d:
            return d[node]
        else:
            tmp = Node(node.val, [])
            d[node] = tmp
            neighbors = [self.dfs(n, d) for n in node.neighbors]
            tmp.neighbors = neighbors
            return tmp

