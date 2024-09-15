# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation

# think of it as a merge K-sorted list
# for the below input:
#     [1,7,11],
#     [2,4,6]
# we have 3 sorted list
# (1, 2) -> (1, 4) -> (1, 6)
# (7, 2) -> (7, 4) -> (7, 6)
# (11,2) -> (11,4) -> (11,6)

from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        rst = []
        heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        for _ in range(k):
            if heap:
                _, i, j = heapq.heappop(heap)
                rst.append([nums1[i], nums2[j]])
                if j+1 < len(nums2):
                    heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            else:
                break
        return rst


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            (
                [1,7,11],
                [2,4,6],
                3
            ),
            [[1,2],[1,4],[1,6]]
        ),
        (
            (
                [1,1,2],
                [1,2,3],
                2
            ),
            [[1,1],[1,1]]
        ),
        (
            (
                [1,2],
                [3],
                3
            ),
            [[1,3],[2,3]]
        ),
        (
            (
                [1,2],
                [1,3],
                4
            ),
            [[1,1],[2,1],[1,3],[2,3]]
        ),
        (
            (
                [1,2,4,5,6],
                [3,5,7,9],
                3
            ),
            [[1,3],[2,3],[1,5]]
        ),
    ]
    test(Solution().kSmallestPairs, test_data)

