from common import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        queue = [root, None]
        level = []
        l = 1
        while queue:
            node = queue.pop(0)
            if node is None:
                if l % 2 == 0:
                    res.append(level[::-1])
                else:
                    res.append(level)
                level = []
                l += 1
                if not queue:
                    break
                else:
                    queue.append(None)
            else:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            TreeNode.create([3,9,20,None,None,15,7]),
            [
                [3],
                [20,9],
                [15,7]
            ]
        ),
        (
            None,
            []
        )
    ]
    test(Solution().zigzagLevelOrder, test_data)

