class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        self.offset = 0
        nodes = preorder.split(',')
        return self.recursive(nodes) and self.offset == len(nodes)

    def recursive(self, nodes):
        if not (self.offset < len(nodes)):
            return False # incomplete
        root = nodes[self.offset]
        self.offset += 1
        if root == '#':
            return True
        else:
            # left & right
            if self.recursive(nodes) and self.recursive(nodes):
                return True
            return False


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            '9,3,4,#,#,1,#,#,2,#,6,#,#',
            True
        ),
        (
            '1,#',
            False
        ),
        (
            '9,#,#,1',
            False
        )
    ]
    test(Solution().isValidSerialization, test_data)
