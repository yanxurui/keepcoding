from typing import List
# https://leetcode.com/problems/frog-jump/discuss/88824/Very-easy-to-understand-JAVA-solution-with-explanations

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {stone:set() for stone in stones}
        d[stones[0]].add(1)
        for stone in stones:
            for step in d[stone]:
                reach = stone+step
                if reach == stones[-1]:
                    return True
                if reach in d:
                    if step-1 > 0:
                        d[reach].add(step-1)
                    d[reach].add(step)
                    d[reach].add(step+1)
        return False


# TLE
class Solution2:
    def canCross(self, stones: List[int]) -> bool:
        return self.dfs(stones, 0, 1)

    def dfs(self, stones, i, k):
        # jump from index i by k units
        n = len(stones)
        if i == n-1:
            # arrive at the last stone
            return True
        # jump to j
        j = self.bs(stones, i+1, len(stones)-1, stones[i]+k)
        if j > 0:
            return self.dfs(stones, j, k-1) or self.dfs(stones, j, k) or self.dfs(stones, j, k+1)
        else:
            return False

    def bs(self, stones, l, h, t):
        while l <= h:
            m = (l+h)//2
            if stones[m] == t:
                return m
            elif stones[m] < t:
                l = m+1
            else:
                h = m-1
        return -1


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [0,1,3,5,6,8,12,17],
            True
        ),
        (
            [0,1,2,3,4,8,9,11],
            False
        )
    ]
    test(Solution().canCross, test_data)

