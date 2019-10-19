# https://leetcode.com/problems/additive-number/discuss/75567/Java-Recursive-and-Iterative-Solutions

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n//2+1):
            j = 1
            while max(i, j) <= n - i - j:
                if self.isValid(num, i, j):
                    return True
                j += 1
        return False

    def isValid(self, num, i, j):
        if num[0] == '0' and i > 1:
            return False
        if num[i] == '0' and j > 1:
            return False
        a = int(num[:i])
        b = int(num[i:i+j])
        k = i + j
        while k<len(num):
            s = a + b
            a = b
            b = s
            s = str(s)
            if not (num[k:].startswith(s)):
                return False
            k = k + len(s)
        assert k == len(num)
        return True


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            '112358',
            True
        ),
        (
            '199100199',
            True
        ),
        (
            "123",
            True
        ),
        (
            "211738",
            True
        ),
        (
            "199111992",
            True
        )
    ]
    test(Solution().isAdditiveNumber, test_data)
