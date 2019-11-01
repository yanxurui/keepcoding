from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        path = []
        
        self.search(root, target, path)
        rst = []
        path = path[::-1]
        for dis, cur in enumerate(path):
            if dis == 0:
                assert cur is target
                self.dfs(cur, K, rst)
            elif dis == K:
                rst.append(cur.val)
            elif dis < K:
                if cur.left is path[dis-1]:
                    self.dfs(cur.right, K-dis-1, rst)
                else:
                    self.dfs(cur.left, K-dis-1, rst)
            else:
                break
        return rst

    def dfs(self, root, depth, rst):
        if root is None:
            return
        if depth == 0:
            rst.append(root.val)
        elif depth > 0:
            self.dfs(root.left, depth-1, rst)
            self.dfs(root.right, depth-1, rst)

    def search(self, root, target, path):
        if root is None:
            return False
        path.append(root)
        if root is target:
            return True
        if self.search(root.left, target, path) or self.search(root.right, target, path):
            return True
        else:
            path.pop()
            return False


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    root1 = TreeNode.create([3,5,1,6,2,0,8,None,None,7,4])
    root2 = TreeNode.create([0,1,None,3,2])
    test_data = [  
        (
            (
                root1,
                root1.left, 2
            ),
            [7,4,1]
        ),
        (
            (
                root2,
                root2.left.right, 1
            ),
            [1]
        ),
    ]
    test(Solution().distanceK, test_data)

