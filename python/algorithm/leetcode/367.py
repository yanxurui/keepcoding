class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return self.NewtonMethod(num)

    def NewtonMethod(self, num):
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            16,
            True
        ),
        (
            14,
            False
        ),
        (
            2,
            False
        )
    ]
    test(Solution().isPerfectSquare, test_data)

