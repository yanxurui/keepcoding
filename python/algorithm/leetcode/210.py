# https://leetcode.com/problems/course-schedule-ii/discuss/59317/Two-AC-solution-in-Java-using-BFS-and-DFS-with-explanation

from collections import defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        edges = [[] for i in range(numCourses)]
        inLinks = [0 for i in range(numCourses)]
        for v1, v2 in prerequisites:
            edges[v2].append(v1)
            inLinks[v1] += 1
        toVisit = []
        res = []
        for i in range(numCourses):
            if inLinks[i] == 0:
                toVisit.append(i)
        while toVisit:
            v = toVisit.pop(0)
            res.append(v)
            for v2 in edges[v]:
                inLinks[v2] -= 1
                if inLinks[v2] == 0:
                    toVisit.append(v2)
        return res if len(res) == numCourses else []


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                2,
                [[1,0]]
            ),
            [0,1]
        ),
        (
            (
                4,
                [[1,0],[2,0],[3,1],[3,2]]
            ),
            [0,1,2,3]
        ),
        (
            (
                3,
                [[1,0],[2,0],[2,1]]
            ),
            [0,1,2]
        )
    ]
    test(Solution().findOrder, test_data)
