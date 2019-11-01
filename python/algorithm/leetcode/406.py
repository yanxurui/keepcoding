from typing import List
import heapq

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        rst = [0] * len(people)
        heap = [(h, -k) for h, k in people]
        heapq.heapify(heap)
        while heap:
            h, k = heapq.heappop(heap)
            k = -k
            p = -1
            cnt = 0
            # find the (k+1) th empty slot
            while cnt <= k:
                p += 1
                if rst[p] == 0:
                    cnt += 1
                # find an empty slot
            rst[p] = [h, k]
        return rst

# https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC%2B%2BJava-Solution

import itertools
class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        rst = []
        for _, g in itertools.groupby(sorted(people, reverse=True), key=lambda p:p[0]):
            for h, k in sorted(g, key=lambda p:p[1]):
                rst.insert(k, [h, k])
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
            [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        )
    ]
    test(Solution2().reconstructQueue, test_data)

