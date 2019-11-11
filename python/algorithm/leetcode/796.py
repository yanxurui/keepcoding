class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A+A

if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'abcde',
                'cdeab'
            ),
            True
        ),
        (
            (
                'abcde',
                'abced'
            ),
            False
        ),
    ]
    test(Solution().rotateString, test_data)

