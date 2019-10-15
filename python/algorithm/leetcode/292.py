class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            4,
            False
        ),
        (
            5,
            True
        ),
        
        
    ]
    test(Solution().canWinNim, test_data)

