from typing import List
from collections import defaultdict
from string import ascii_lowercase as lowercase

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        letters = set(lowercase)
        b, e = 0, 0
        paragraph = paragraph.lower()
        count = defaultdict(int)
        import pdb
        # pdb.set_trace()
        while True:
            while b < len(paragraph) and paragraph[b] not in letters:
                b += 1
            if b >= len(paragraph):
                break
            e = b+1
            while e < len(paragraph) and paragraph[e] in letters:
                e += 1
            word = paragraph[b:e]
            if word not in banned:
                count[word] += 1
            b = e + 1
        max_pair = max(count.items(), key=lambda item: item[1])
        return max_pair[0]


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'Bob hit a ball, the hit BALL flew far after it was hit.',
                ["hit"]
            ),
            'ball'
        ),
        (
            (
                "Bob",
                []
            ),
            'bob'
        ),
    ]
    test(Solution().mostCommonWord, test_data)

