# https://leetcode.com/problems/reorganize-string/discuss/113435/4-lines-Python
import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) == 1:
            return S
        count = Counter(S)
        heap = [(k, c) for c,k in count.items()]
        heapq.heapify(heap)
        i = 1
        n = len(S)
        buf = [0] * n
        while heap:
            k, c = heapq.heappop(heap)
            for _ in range(k):
                
                buf[i] = c
                i += 2
                if i >= n:
                    i = 0
        if buf[-1] == buf[-2]:
            return ''
        else:
            return ''.join(buf)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'aab',
            'aba'
        ),
        (
            'aaab',
            ''
        ),
        (
            "abbabbaaab",
            "bababababa"
        ),
        (
            'a',
            'a'
        ),
    ]
    test(Solution().reorganizeString, test_data)

