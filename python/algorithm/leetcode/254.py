from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def rec(n, start, l, ans):
            if l:
                if n == 1:
                    ans.append(l)
                    return
                else:
                    ans.append(l+[n])
            i = start
            while i * i < n:
                if n % i == 0:
                    rec(n//i, i, l+[i], ans)
                i += 1

        ans = []
        rec(n, 2, [], ans)
        return ans


if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            1,
            []
        ),
        (
            12,
            [[2,6],[3,4],[2,2,3]]
        ),
        (
            37,
            []
        )
    ]
    test(Solution().getFactors, test_data, compare=unordered_equal)

