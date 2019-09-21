# https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.kv = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.kv.get(key)
        if node != None:
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.kv.get(key)
        if node:
            self._remove(node)
            del self.kv[node.key]
        if len(self.kv) >= self.capacity:
            node = self.head.next
            self._remove(node)
            del self.kv[node.key]
        node = Node(key, value)
        self._add(node)
        self.kv[key] = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


    cache = LRUCache(2)
    assert cache.get(2) == -1
    cache.put(2, 6)
    assert cache.get(1) == -1
    cache.put(1, 5)
    cache.put(1, 2)
    assert cache.get(1) == 2
    assert cache.get(2) == 6
