# https://leetcode.com/problems/design-skiplist/discuss/393713/Python-1-node-per-value-and-100
from random import random
from math import log

class Node:
    def __init__(self, val, levels):
        self.val = val
        self.levels = [None] * levels

class Skiplist:

    def __init__(self):
        self.head = Node(-1, 16)

    def _iter(self, target):
        cur = self.head
        for l in range(15, -1, -1):
            while True:
                future = cur.levels[l]
                if future and target > future.val:
                    cur = future
                else:
                    break
            yield cur, l # cur is not None

    def search(self, target: int) -> bool:
        for cur,l in self._iter(target):
            pass
        nxt = cur.levels[0]
        return nxt and nxt.val == target

    def add(self, num: int) -> None:
        node_levels = min(16, 1 + int(log(1/random(), 2)))
        node = Node(num, node_levels)
        for cur, l in self._iter(num):
            if l < node_levels:
                node.levels[l] = cur.levels[l]
                cur.levels[l] = node

    def erase(self, num: int) -> bool:
        rst = False
        for cur, l in self._iter(num):
            nxt = cur.levels[l]
            if nxt and nxt.val == num:
                rst = True
                cur.levels[l] = cur.levels[l].levels[l]
        return rst



# Your Skiplist object will be instantiated and called as such:

skiplist = Skiplist()

skiplist.add(1)
skiplist.add(2)
skiplist.add(3)
assert skiplist.search(0) is False
skiplist.add(4)
assert skiplist.search(1)
assert skiplist.erase(0) is False
assert skiplist.erase(1)
assert skiplist.search(1) is False