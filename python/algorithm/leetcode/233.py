# https://leetcode.com/problems/number-of-digit-one/discuss/64381/4%2B-lines-O(log-n)-C%2B%2BJavaPython

class Solution:
    def countDigitOne(self, n: int) -> int:
        ones = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            # >= 2: a/10+1
            # 0, 1: a/10
            ones += (a+8)//10 * m
            # == 1
            if a%10 == 1:
                ones += (b+1)
            m *= 10
        return ones


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (13),
            6
        ),
    ]
    test(Solution().countDigitOne, test_data)
