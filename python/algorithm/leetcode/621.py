from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0:
            return 0
        count = Counter(tasks)
        mk, f = self.maxValuOfDict(count)
        count_most_frequent = len(mk)
        # v-1 slots
        # at least n distinct tasks in a slot
        # idles = empty - available
        idles = (f-1) * (n-(count_most_frequent-1)) - (len(tasks) - count_most_frequent*f)
        rst = len(tasks)
        if idles >= 0:
            rst += idles
        return rst

    def maxValuOfDict(self, d):
        mk = []
        mv = None
        for k,v in d.items():
            if mv is None or v > mv:
                mk = [k]
                mv = v
            elif v == mv:
                mk.append(k)
        return mk, mv


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                ["A","A","A","B","B","B"],
                2
            ),
            8
        ),
        (
            (
                ["A","A","A","A","A","A","B","C","D","E","F","G"],
                2
            ),
            16
        ),
        (
            (
                ['A'],
                2
            ),
            1
        ),
        (
            (
                [],
                2
            ),
            0
        ),
    ]
    test(Solution().leastInterval, test_data)

