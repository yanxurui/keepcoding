# https://leetcode.com/problems/self-crossing/discuss/79131/Java-Oms-with-explanation

from typing import List

class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        for i in range(3, len(x)):
            # fourth line crosses first line
            if x[i-1] <= x[i-3] and x[i] >= x[i-2]:
                return True
            # fifth line meets first line
            if i>= 4 and x[i-1] == x[i-3] and x[i]+x[i-4] >= x[i-2]:
                return True
            # sixth line crosses first line
            if i >= 5 and x[i-2] >= x[i-4] and x[i-1]+x[i-5] >= x[i-3] and x[i-1] <=x[i-3] and x[i]+x[i-4] >= x[i-2]:
                return True
        return False


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            [2,1,1,2],
            True
        ),
        (
            [1,2,3,4],
            False
        ),
        (
            [1,1,1,1],
            True
        ),
        (
            [1,1,2,3,2,1,1],
            False
        ),
        (
            [1,1,2,1,1],
            True
        ),
        (
            [1,1,2,2,1,1],
            True
        ),
        (
            [3,3,4,2,2],
            False
        )
    ]
    test(Solution().isSelfCrossing, test_data)
