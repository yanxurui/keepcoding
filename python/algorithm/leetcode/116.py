from common import TreeNode
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        queue = [root, None]
        current = None
        while queue:
            node = queue.pop(0)
            if node is None:
                # end of this level
                if not queue:
                    break
                else:
                    queue.append(None)
                current = None
            else:
                if current is not None:
                    current.next = node
                current = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

