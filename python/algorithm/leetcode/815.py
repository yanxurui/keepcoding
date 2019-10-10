from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes, S: int, T: int) -> int:
        d = defaultdict(list)
        for i,r in enumerate(routes):
            for s in r:
                d[s].append(i)
        n = 0
        visited = set()
        Q = [S]

        while Q:
            Stops = Q
            Q = []
            for S in Stops: # current stop
                if S == T:
                    return n
                for b in d[S]: # buses that I can take
                    if b in visited:
                        continue
                    visited.add(b)
                    Q.extend(routes[b]) # stops that I can go by one bus
            n += 1
        return -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [[1, 2, 7], [3, 6, 7]],
                1,6
            ),
            2
        ),
        (
            (
                [[1, 2, 3, 7], [3, 6, 7]],
                1, 3
            ),
            1
        ),
        (
            (
                [[1, 2, 7], [3, 6, 8]],
                1, 8
            ),
            -1
        ),
    ]
    test(Solution().numBusesToDestination, test_data)
