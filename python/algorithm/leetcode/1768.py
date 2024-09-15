class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        b = []
        while i < len(word1) and i < len(word2):
            b.append(word1[i])
            b.append(word2[i])
            i += 1
        if i < len(word1):
            b.append(word1[i:])
        elif i < len(word2):
            b.append(word2[i:])
        return ''.join(b)



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            ('abc', 'pqr'),
            'apbqcr'
        ),
        (
            ('ab', 'pqrs'),
            'apbqrs'
        )
    ]
    test(Solution().mergeAlternately, test_data)

