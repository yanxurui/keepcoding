class Solution:
    def romanToInt(self, s: str) -> int:
        


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ('III'),
            3
        ),
        (
            ('LVIII'),
            58
        ),
        (
            ('MCMXCIV'),
            1994
        ),
        
    ]
    test(Solution().romanToInt, test_data)
