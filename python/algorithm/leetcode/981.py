from collections import defaultdict
class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(list)


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.d[key].append((timestamp, value))


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.d:
            return self.bs(self.d[key], timestamp)
        else:
            return ''
    def bs(self, arr, k):
        if len(arr) == 0 or arr[0][0] > k:
            return ''
        l, r = 0, len(arr)-1
        while l <= r:
            m = l + (r-l)//2
            if k < arr[m][0]:
                r = m - 1
            else:
                l = m + 1
        # l points to the first one that is greater than k
        return arr[l-1][1]


# Your TimeMap object will be instantiated and called as such:
kv = TimeMap()
kv.set('foo','bar',1)
assert kv.get('foo',1) == 'bar'
assert kv.get('foo',3) == 'bar'
kv.set('foo','bar2',2)
assert kv.get("foo", 4) == "bar2"
assert kv.get("foo", 5) == "bar2"
assert kv.get("foo", 0) == ""
assert kv.get("foo2", 1) == ""




kv = TimeMap()
kv.set('love','high',10)
kv.set('love','low',20)
assert kv.get('love',5) == ''
assert kv.get('love',10) == 'high'
assert kv.get('love',15) == 'high'
assert kv.get('love',20) == 'low'
assert kv.get('love',25) == 'low'
