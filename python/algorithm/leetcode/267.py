from typing import List
from collections import Counter

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        kv = Counter(s)
        mid = [k for k,v in kv.items() if v%2 != 0]
        if len(mid) > 1:
            return []
        mid = mid[0] if mid else ''
        half = ''.join([k*(v//2) for k,v in kv.items()]) # mid is zero-ed
        half = list(half) # list of chars

        def permute(visited, tmp, ans):
            if len(tmp) == len(half):
                ans.append(''.join(tmp) + mid + (''.join(tmp))[::-1])
                return
            for i,c in enumerate(half):
                if visited[i] or (i > 0 and half[i] == half[i-1] and not visited[i-1]):
                    continue
                visited[i] = True
                tmp.append(c)
                permute(visited, tmp, ans)
                tmp.pop()
                visited[i] = False
        visited = [False for c in half]
        tmp = []
        ans = []
        permute(visited, tmp, ans)
        return ans


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            'aabb',
            ["abba","baab"]
        ),
        (
            'abc',
            []
        )
    ]
    test(Solution().generatePalindromes, test_data, compare=unordered_equal)

