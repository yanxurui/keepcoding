# https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n:
            n //= 5
            count += n
        return count


if __name__ == '__main__':
    from testfunc import test
    
    test_data = [
        (
            (3),
            0
        ),
        (
            (5),
            1
        )
    ]
    test(Solution().trailingZeroes, test_data)
