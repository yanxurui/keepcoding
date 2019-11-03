from typing import List
from collections import defaultdict
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        rst = 0
        sorted_arr = sorted(arr)
        d = defaultdict(int) # how many digits needed
        cnt = 0 # how many unmatched digits
        for i in range(len(arr)):
            b = sorted_arr[i]
            a = arr[i]
            if d[b] == 0:
                cnt += 1
            d[b] += 1
            d[a] -= 1
            if d[a] == 0:
                cnt -= 1
            if cnt == 0:
                rst += 1
                assert not any(d.values())
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [5,4,3,2,1],
            1
        ),
        (
            [2,1,3,4,4],
            4
        ),
    ]
    test(Solution().maxChunksToSorted, test_data)

