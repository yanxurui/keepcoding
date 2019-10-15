from typing import List

class Solution:
    # def hIndex(self, citations: List[int]) -> int:
    #     citations.sort()
    #     n = len(citations)
    #     for i in citations:
    #         if i >= n:
    #             return n
    #         else:
    #             n -= 1
    #     return 0
    def hIndex(self, citations: List[int]) -> int:
        # https://leetcode.com/problems/h-index/discuss/70768/Java-bucket-sort-O(n)-solution-with-detail-explanation
        n = len(citations)
        buckets = [0] * (n+1)
        for c in citations:
            if c > n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        cnt = 0
        for i in range(n, -1, -1):
            cnt += buckets[i]
            if cnt >= i:
                # i papers have at least i citations
                return i


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            [3,0,6,1,5],
            3
        )
    ]
    test(Solution().hIndex, test_data)
