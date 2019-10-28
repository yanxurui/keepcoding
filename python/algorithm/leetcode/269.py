# https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time
from typing import List
from collections import defaultdict

class Solution:
    def alienDictonary(self, words):
        edges = defaultdict(set)
        degrees = defaultdict(int)
        chars = set()
        N = 0
        for i in range(len(words)):
            w1 = words[i]
            chars |= set(w1)
            for j in range(i+1, len(words)):
                # find the first mismatching char
                w2 = words[j]
                chars |= set(w2)
                for k in range(min(len(w1), len(w2))):
                    if w1[k] != w2[k]:
                        break
                if k == min(len(w1), len(w2)):
                    continue
                if w2[k] not in edges[w1[k]]:
                    edges[w1[k]].add(w2[k])
                    degrees[w2[k]] += 1
                    N += 1 # sum of edges
        # topological sort
        rst = []
        q = [c for c in chars if degrees[c] == 0]
        while q:
            v1 = q.pop(0)
            rst.append(v1)
            for v2 in edges[v1]:
                degrees[v2] -= 1
                N -= 1
                if degrees[v2] == 0:
                    q.append(v2)
        if N == 0:
            return ''.join(rst)
        else:
            return ''


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [
              "wrt",
              "wrf",
              "er",
              "ett",
              "rftt"
            ],
            'wertf'
        ),
        (
            [
              "z",
              "x",
              "z"
            ],
            ''
        ),
        (
            [
              "z",
              "x"
            ],
            'zx'
        ),
    ]
    test(Solution().alienDictonary, test_data)

