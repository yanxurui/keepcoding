# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        self.count = k
        self.rst = None
        self.util(root)
        return self.rst

    def util(self, root):
        if root is None:
            return
        self.util(root.left)
        self.count -= 1
        if self.count == 0:
            self.rst = root.val
        self.util(root.right)


class Solution2:
    def kthSmallest(self, root, k: int) -> int:
        i = 0
        stack = []
        p = root
        while True:
            # push left: if p has left, put in stack
            while p:
                stack.append(p)
                p = p.left
            # process p
            if stack:
                p = stack.pop()
                i += 1
                if i == k:
                    return p.val
                p = p.right
            else:
                break
        return None


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            (
                TreeNode.create([3,1,4,None,2]),
                1
            ),
            1
        ),
        (
            (
                TreeNode.create([3,1,4,None,2]),
                2
            ),
            2
        ),
        (
            (
                TreeNode.create([5,3,6,2,4,None,None,1]),
                3
            ),
            3
        ),
        (
            (
                TreeNode.create([31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9]),
                1
            ),
            0
        )
    ]
    test(Solution2().kthSmallest, test_data)
