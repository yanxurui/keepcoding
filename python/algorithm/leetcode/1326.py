from typing import List
from collections import defaultdict

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # convert this problem to jump ii
        canJump = defaultdict(int)
        for i in range(n+1):
            left = max(0, i-ranges[i])
            right = i+ranges[i]
            canJump[left] = max(canJump[left], right)

        # sort by key ascending
        # each item represents (current position, where it can jump)
        canJump = sorted(canJump.items(), key=lambda item: item[0])

        # solve problem jump ii
        i = 0
        farToJump = 0
        ans = 0
        while farToJump < n:
            tmp = farToJump
            while i < len(canJump) and canJump[i][0] <= tmp:
                farToJump = max(farToJump, canJump[i][1])
                i += 1
            if farToJump == tmp:
                return -1
            ans += 1
        return ans

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                5,
                [3,4,1,1,0,0]
            ),
            1
        ),
        (
            (
                3,
                [0,0,0,0]
            ),
            -1
        ),
        (
            (
                7,
                [1,2,1,0,2,1,0,1]
            ),
            3
        ),
    ]
    test(Solution().minTaps, test_data)

