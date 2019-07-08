# ugly and slow

from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        layer = [root.left, root.right]
        l = 1
        while True:
            n = 2**(l-1)
            for left, right in zip(layer[:n], layer[n:][::-1]):
                if left is None and right is None:
                    continue
                if left is None or right is None:
                    return False
                if left.val != right.val:
                    return False
            next_layer = []
            end = True
            for node in layer:
                if node is None:
                    next_layer.append(None)
                    next_layer.append(None)
                else:
                    end = False
                    next_layer.append(node.left)
                    next_layer.append(node.right)
            layer = next_layer
            l += 1
            if end:
                break
        return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([1,2,2,3,4,4,3]),
            True
        ),
        (
            TreeNode.create([1,2,2,None,3,None,3]),
            False
        )
    ]
    test(Solution().isSymmetric, test_data)

