# https://leetcode.com/problems/minimize-malware-spread-ii/discuss/184129/python-solution-with-my-thinking-process-(with-extra-Chinese-explanation)
from collections import defaultdict

class Solution:
    def minMalwareSpread(self, graph, initial) -> int:
        # d[j] is the set of nodes that can directly infect node j
        d = defaultdict(list)
        # BFS
        for infected in initial:
            q = [infected]
            visited = set()
            while q:
                i = q.pop()
                for j, e in enumerate(graph[i]):
                    if e == 1 and j not in visited and j not in initial:
                        visited.add(j)
                        d[j].append(infected)
                        q.append(j)
        # cnt[i] is the number of nodes that can only be directly infected by node i
        cnt = [0] * len(graph)
        for k, s in d.items():
            if len(s) == 1:
                cnt[s[0]] += 1
        if max(cnt) == 0:
            return min(initial)
        else:
            return cnt.index(max(cnt))



if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            (
                [
                    [1,1,0],
                    [1,1,0],
                    [0,0,1]
                ],
                [0,1]
            ),
            0
        ),
        (
            (
                [
                    [1,1,0],
                    [1,1,1],
                    [0,1,1]
                ],
                [0,1]
            ),
            1
        ),
        (
            (
                [
                    [1,1,0,0],
                    [1,1,1,0],
                    [0,1,1,1],
                    [0,0,1,1]
                ],
                [0,1]
            ),
            1
        ),
        
    ]
    test(Solution().minMalwareSpread, test_data)
