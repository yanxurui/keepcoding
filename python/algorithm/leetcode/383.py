from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        magazine = Counter(magazine)
        for c, f in note.items():
            if c not in magazine or magazine[c] < f:
                return False
        return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ('a', 'b'),
            False
        ),
        (
            ('aa', 'ab'),
            False
        ),
        (
            ('aa', 'aab'),
            True
        )
    ]
    test(Solution().canConstruct, test_data)

