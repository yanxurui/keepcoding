from typing import List
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        rst = []
        for w, c in Counter(A.split(' ') + B.split(' ')).items():
            if c == 1:
                rst.append(w)
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                'this apple is sweet',
                'this apple is sour'
            ),
            ["sweet","sour"]
        ),
        (
            (
                'apple apple',
                'banana'
            ),
            ['banana']
        ),
    ]
    test(Solution().uncommonFromSentences, test_data)

