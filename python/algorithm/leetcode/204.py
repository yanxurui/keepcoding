class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True for i in range(n)]
        for i in range(2, n):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (10),
            4
        ),
        (
            (3),
            1
        )
    ]
    test(Solution().countPrimes, test_data)
