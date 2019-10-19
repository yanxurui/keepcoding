from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        idx = [0] * len(primes)
        for i in range(n-1):
            ugly.append(min([ugly[idx[i]]*p for i,p in enumerate(primes)]))
            for i, p in enumerate(primes):
                if ugly[-1] == p * ugly[idx[i]]:
                    idx[i] += 1
        return ugly[-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                12,
                [2,7,13,19]
            ),
            32
        )
    ]
    test(Solution().nthSuperUglyNumber, test_data)
