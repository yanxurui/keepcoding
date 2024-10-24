from typing import List
class Solution:
    def sumOfDigits(self, n):
        s = 0
        while n > 0:
            s = s + n%10
            n = n // 10
        return s

    def maximumSum(self, nums: List[int]) -> int:
        r = -1
        d = {}
        for n in nums:
            k = self.sumOfDigits(n)
            m = d.get(k)
            if m and m + n > r:
                r = m + n
            if m is None or n > m:
                d[k] = n
        return r

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [18,43,36,13,7],
            54
        ),
        (
            [10,12,19,14],
            -1
        ),
    ]
    test(Solution().maximumSum, test_data)
