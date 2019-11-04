# https://leetcode.com/problems/integer-replacement/discuss/87920/A-couple-of-Java-solutions-with-explanations

class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            if n % 2 == 0:
                n = n >> 1
            else:
                if n == 3 or n % 4 == 1:
                    n -= 1
                else:
                    n += 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            8,
            3
        ),
        (
            7,
            4
        ),
        (
            1,
            0
        ),
        (
            3,
            2
        ),
    ]
    test(Solution().integerReplacement, test_data)
