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
        # pre-order traverse
        buf = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                buf.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop().right
        return ','.join(map(str, buf))
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        nums = list(map(int, data.split(',')))
        return self.deserializeUtil(nums, 0, len(nums)-1)

    def deserializeUtil(self, nums, i, j):
        if i > j:
            return None
        root = TreeNode(nums[i])
        m = self.bs(nums, i+1, j, nums[i])
        root.left = self.deserializeUtil(nums, i+1, m-1)
        root.right = self.deserializeUtil(nums, m, j)
        return root

    def bs(self, nums, l, r, t):
        while l <= r:
            m = l + (r-l)//2
            if t > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l
