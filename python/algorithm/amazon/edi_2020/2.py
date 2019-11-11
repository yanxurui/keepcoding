# exception during some test cases

from collections import defaultdict
import traceback
def criticalConnection(numOfServers, numOfConnections, connections):
    # WRITE YOUR CODE HERE
    if numOfConnections == 0:
        return []
    graph = defaultdict(list)
    servers = set()
    for conn in connections:
        servers.add(conn[0])
        servers.add(conn[1])
        graph[conn[0]].append(conn[1])
        graph[conn[1]].append(conn[0])
    connections = set(map(tuple, (map(sorted, connections))))
    rank = defaultdict(lambda: int(-1))
    def dfs(node, depth):
        if rank[node] >= 1:
            return rank[node]
        rank[node] = depth
        min_back_depth = depth
        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1:
                # parent node
                continue
            back_depth = dfs(neighbor, depth + 1)
            if back_depth <= depth:
                connections.discard(tuple(sorted((node, neighbor))))
            min_back_depth = min(min_back_depth, back_depth)
        return min_back_depth

    for s in servers:
        dfs(s, 1)
    rst = list(map(list, connections))
    return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                5,5,
                [
                    [1,2],
                    [1,3],
                    [3,4],
                    [1,4],
                    [4,5],
                ]
            ),
            [
                [1,2],
                [4,5],
            ]
        ),
        (
            (
                6,5,
                [
                    [1,2],
                    [2,3],
                    [3,4],
                    [4,5],
                    [6,3],
                ]
            ),
            [
                [1,2],
                [2,3],
                [3,4],
                [3,6],
                [4,5],
            ]
        ),
        (
            (
                1,0,
                [
                ]
            ),
            [
            ]
        ),
        (
            (
                3,3,
                [
                    [1,2],
                    [2,3],
                    [1,3],
                ]
            ),
            [
            ]
        ),
        (
            (
                2,2,
                [
                    [1,2],
                    [2,1]
                ]
            ),
            [
                [1,2]
            ]
        ),

    ]
    test(criticalConnection, test_data)
