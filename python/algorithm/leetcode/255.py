from typing import List
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # convert to in-order traverse
        stack = []
        minVal = None
        for n in preorder:
            if minVal and minVal > n:
                return False
            while stack and n > stack[-1]:
                # pop its parent and the parent's left sub-tree
                minVal = stack.pop()
            stack.append(n)
        return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [5,2,1,3,6],
            True
        ),
        (
            [5,2,6,1,3],
            False
        )
    ]
    test(Solution().verifyPreorder, test_data)

