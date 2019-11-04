from typing import List
from collections import deque
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        q = deque([S])
        for i,c in enumerate(S):
            if c.isalpha():
                l = len(q)
                for _ in range(l):
                    s = q.popleft()
                    q.append(s[:i] + c.lower() + s[i+1:])
                    q.append(s[:i] + c.upper() + s[i+1:])
        return list(q)


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            'a1b2',
            ["a1b2", "a1B2", "A1b2", "A1B2"]
        ),
        (
            '3z4',
            ["3z4", "3Z4"]
        ),
        (
            '12345',
            ["12345"]
        ),
    ]
    test(Solution().letterCasePermutation, test_data)

