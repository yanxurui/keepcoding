class LinkedList:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None

    def find(self, k):
        prev = cur = self
        while cur is not None and cur.k != k:
            prev = cur
            cur = cur.next
        return prev


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.index = [LinkedList(-1,0) for i in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ll = self.index[key % self.size]
        prev = ll.find(key)
        if prev.next is None:
            # insert
            prev.next = LinkedList(key, value)
        else:
            # update
            prev.next.v = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ll = self.index[key % self.size]
        prev = ll.find(key)
        if prev.next is None:
            return -1
        else:
            return prev.next.v
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ll = self.index[key % len(self.index)]
        prev = ll.find(key)
        if prev.next is None:
            return
        else:
            prev.next = prev.next.next
    
    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)]
obj = MyHashMap()
for k in range(100000+1):
    obj.put(k, k)
