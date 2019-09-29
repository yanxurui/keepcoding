# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
# detect cycle in a directed graph

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(list)
        for v1, v2 in prerequisites:
            edges[v1].append(v2)
        return not self.isCycle(range(numCourses), edges)

    def isCycle(self, vertices, edges):
        visited = defaultdict(lambda:False)
        recStack = defaultdict(lambda:False)
        for v in vertices:
            if not visited[v] and self.isCycleUtil(v, edges, visited, recStack):
                return True
        return False

    def isCycleUtil(self, v, edges, visited, recStack):
        visited[v] = True
        recStack[v] = True
        for v2 in edges[v]:
            if visited[v2]:
                if recStack[v2] is True:
                    return True
            else:
                if self.isCycleUtil(v2, edges, visited, recStack):
                    return True
        # pop
        recStack[v] = False
        return False


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (
                2,
                [[1,0]]
            ),
            True
        ),
        (
            (
                2,
                [[1,0],[0,1]]
            ),
            False
        ),
        (
            (
                3,
                [[0,1],[1,2],[2,0]]
            ),
            False
        )
    ]
    test(Solution().canFinish, test_data)
