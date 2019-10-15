class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern) != len(str.split(' ')):
            return False
        d1 = {}
        d2 = {}
        for c, w in zip(pattern, str.split(' ')):
            if c not in d1 and w not in d2:
                d1[c] = w
                d2[w] = c
            elif c in d1 and w in d2:
                # if not (d1[c] == w and d2[w] == c):
                if not (d1[c] == w):
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'abba',
                'dog cat cat dog'
            ),
            True
        ),
        (
            (
                'abba',
                'dog cat cat fish'
            ),
            False
        ),
        (
            (
                'aaaa',
                'dog cat cat dog'
            ),
            False
        ),
        (
            (
                'aaaa',
                'cat cat cat cat'
            ),
            True
        ),
        (
            (
                "abba",
                "dog dog dog dog"
            ),
            False
        ),
        (
            (
                "aaa",
                "aa aa aa aa"
            ),
            False
        )
        
    ]
    test(Solution().wordPattern, test_data)

