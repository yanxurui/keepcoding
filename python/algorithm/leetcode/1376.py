from typing import List

class Solution:
    def dfs(self, i, manager, informTime, delay):
        if i in delay:
            return delay[i]
        j = manager[i] # manager
        delay[i] = self.dfs(j, manager, informTime, delay) + informTime[j]
        return delay[i]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        delay = {} # delay[i] is the time needed for i to be informed
        delay[headID] = 0
        for i in range(n):
            self.dfs(i, manager, informTime, delay)
        return max(delay)

class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]
        for i, n in enumerate(manager):
            if n >= 0:
                children[n].append(i)
        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]
        return dfs(headID)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                1,
                0,
                [-1],
                [0]
            ),
            0
        ),
        (
            (
                6,
                2,
                [2,2,-1,2,2,2]
                ,
                [0,0,1,0,0,0]
            ),
            1
        ),
    ]
    test(Solution2().numOfMinutes, test_data)

