from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        S = sum(matchsticks)
        if S % 4 != 0:
            return False
        target = S // 4
        matchsticks = sorted(matchsticks, reverse=True)
        return self.dfs(matchsticks, [0]*4, 0, target)

    def dfs(self, matchsticks, sums, index, target):
        if index >= len(matchsticks):
            for i in range(4):
                if sums[i] != target:
                    return False
            return True
        for i in range(4):
            if sums[i] + matchsticks[index] > target:
                continue
            sums[i] += matchsticks[index]
            if self.dfs(matchsticks, sums, index + 1, target):
                return True
            sums[i] -= matchsticks[index]
        return False

if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode
    test_data = [
        (
            [1,1,2,2,2],
            True
        ),
        (
            [3,3,3,3,4],
            False
        )
    ]
    test(Solution().makesquare, test_data)
