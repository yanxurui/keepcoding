# https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C%2B%2B-DP-solution-with-short-explanation

from typing import List

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        tab = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            tab.append(min(2 * tab[p2], 3 * tab[p3], 5 * tab[p5]))
            if tab[-1] == 2 * tab[p2]:
                p2 += 1
            if tab[-1] == 3 * tab[p3]:
                p3 += 1
            if tab[-1] == 5 * tab[p5]:
                p5 += 1
        return tab[n-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            10,
            12
        ),
        (
            1,
            1
        ),
        
    ]
    test(Solution().nthUglyNumber, test_data)
