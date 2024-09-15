# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        l = [root]
        i = 0
        while i < len(l):
            if l[i]:
                l.append(l[i].left)
                l.append(l[i].right)
            i += 1
        assert i == len(l)
        i -= 1
        while not l[i]:
            i -= 1
        return ','.join([str(node.val) if node else 'null' for node in l[:i+1]])


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = []
        root = parent = None
        for node in data.split(','):
            node = None if node == 'null' else TreeNode(int(node))
            if not parent:
                if not q:
                    root = node
                else:
                    parent = q.pop(0) # important
                    parent.left = node
            else:
                parent.right = node
                parent = None
            if node:
                q.append(node)
        return root

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == '__main__':
    from common import TreeNode
    root = TreeNode.create([1,2,3,None,None,4,5])
    codec = Codec()
    assert codec.deserialize(codec.serialize(root)) == root
    root = TreeNode.create([1,None,2])
    codec = Codec()
    assert codec.deserialize(codec.serialize(root)) == root
