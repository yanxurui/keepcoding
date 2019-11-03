class Solution:
    def flipLights(self, n: int, m: int) -> int:
        # k > 0 op 1~3 is equivalent to 1 op 1-3
        # k >= 0 op is equivalent to 0~1 op
        if n == 0:
            return 1
        if m == 0:
            return 1
        # m >= 1
        # n >= 1
        if n == 1:
            return 2
        elif n == 2:
            if m == 1:
                return 3
            else:
                return 4
        elif n >= 3:
            if m == 1:
                return 4
            elif m == 2:
                return 7
            else:
                return 8






if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (1,1),
            2
        ),
        (
            (2,1),
            3
        ),
        (
            (3,1),
            4
        ),
    ]
    test(Solution().flipLights, test_data)

