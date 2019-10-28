import heapq

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for p in points:
            dist = -(p[0]**2 + p[1]**2)
            item = (dist, p)
            if len(heap) == K:
                heapq.heappushpop(heap, item)
            else:
                heapq.heappush(heap, item)
        return [item[1] for item in heap]
        

if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            (
                [[1,3],[-2,2]],
                1
            ),
            [[-2,2]]
        ),
        (
            (
                [[3,3],[5,-1],[-2,4]],
                2
            ),
            [[3,3],[-2,4]]
        )
    ]
    test(Solution().kClosest, test_data, compare=unordered_equal)

