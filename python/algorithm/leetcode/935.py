from collections import defaultdict

class Solution:
    def knightDialer(self, N: int) -> int:
        d = {
            0: set([4, 6]),
            1: set([6, 8]),
            2: set([9, 7]),
            3: set([8, 4]),
            4: set([3, 9, 0]),
            5: set([]),
            6: set([0, 7, 1]),
            7: set([2, 6]),
            8: set([1, 3]),
            9: set([2, 4]),
        }
        rst = 1
        start = {i:1 for i in range(10)}
        for i in range(N):
            rst = sum(start.values()) % (10**9 + 7)
            next = defaultdict(int)
            # jump from s to n
            for s, c in start.items():
                for n in d[s]:
                    next[n] += c
            start = next
        return rst



# https://leetcode.com/problems/knight-dialer/discuss/189252/O(logN)
import numpy as np
class Solution2:
    def knightDialer(self, N: int) -> int:
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        if N == 1:
            return 10
        rst = 1
        N -= 1
        mod = 10**9 + 7
        while N:
            if N%2 == 1:
                rst = rst * M % mod
            M = M*M % mod
            N //= 2
        return int(np.sum(rst)) % mod


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            1,
            10
        ),
        (
            2,
            20
        ),
        (
            3,
            46
        ),
        (
            161,
            533302150
        ),
    ]
    test(Solution2().knightDialer, test_data)
