# https://leetcode.com/problems/h-index-ii/discuss/71063/Standard-binary-search

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l+r)//2
            h = n - mid # papers
            if citations[mid] == h:
                return h
            elif citations[mid] > h:
                r = mid - 1
            else:
                l = mid + 1
        return n - (r+1)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [0,1,3,5,6],
            3
        ),
        (
            [1],
            1
        ),
    ]
    test(Solution().hIndex, test_data)
