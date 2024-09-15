from typing import List

'''
does not work for case 63:
Memory Limit Exceeded
'''
class Solution1:
    def dfs(self, edges, i, visited, tmp):
        # i is the node we are visiting in this round
        # j is the node we are going to visit in the next round
        if i in visited:
            # there are 2 cases:
            # 1. found a circle
            # 2. didn't find a circle but i has been visited before.
            #    no need to proceed anymore
            l = -1
            for k in range(len(tmp)):
                if tmp[k] == i:
                    l = len(tmp) - k
                    break
            return l
        else:
            j = edges[i]
            if j == -1:
                # disconnected
                return -1
            # add i
            visited[i] = True
            return self.dfs(edges, j, visited, tmp + [i])

    def longestCycle(self, edges: List[int]) -> int:
        visited = {}
        an = -1
        for i in range(len(edges)):
            if i not in visited:
                r = self.dfs(edges, i, visited, [])
                if r > an:
                    an = r
        return an
        

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        d = {} # last time node i was visited at step steps[i]
        an = -1
        steps = 0 # total steps
        for i in range(len(edges)):
            s = steps # record the current steps
            d[i] = steps
            j = i # we will start i and walk to the end
            while True:
                steps += 1
                j = edges[j]
                if j == -1:
                    break
                if j in d:
                    if d[j] >= s:
                        # found a circle
                        l = steps - d[j]
                        an = max(an, l)
                    else:
                        pass
                        # we have covered node j before
                    break
                d[j] = steps

        return an


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [3,3,4,2,3],
            3
        ),
        (
            [2,-1,3,1],
            -1
        ),
    ]
    test(Solution().longestCycle, test_data)

