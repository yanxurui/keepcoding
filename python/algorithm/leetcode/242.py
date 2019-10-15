class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'anagram',
                'nagaram'
            ),
            True
        ),
        (
            (
                'rat',
                'car'
            ),
            False
        )
    ]
    test(Solution().isAnagram, test_data)

