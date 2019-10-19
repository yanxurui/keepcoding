# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        tab = {}
        return max(self.robUtil(root, True, tab), self.robUtil(root, False, tab))

    def robUtil(self, root, inc=True, tab=None):
        if not root:
            return 0
        v = tab.get((id(root),inc))
        if v:
            return v
        if inc:
            v = root.val + self.robUtil(root.left, False, tab) + self.robUtil(root.right, False, tab)
        else:
            v = max(self.robUtil(root.left, True, tab), self.robUtil(root.left, False, tab)) \
                   + max(self.robUtil(root.right, True, tab), self.robUtil(root.right, False, tab))
        tab[(id(root),inc)] = v
        return v


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            TreeNode.create([3,2,3,None,3,None,1]),
            7
        ),
        (
            TreeNode.create([3,4,5,1,3,None,1]),
            9
        ),
        (
            TreeNode.create([4,1,None,2,None,3]),
            7
        )
    ]
    test(Solution().rob, test_data)
