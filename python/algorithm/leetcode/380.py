# https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85401/Java-solution-using-a-HashMap-and-an-ArrayList-along-with-a-follow-up.-(131-ms)
from random import randint

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.locs = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        l = self.locs.get(val, None)
        if l is not None:
            return False # exists
        self.nums.append(val)
        self.locs[val] = len(self.nums)-1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        l = self.locs.get(val, None)
        if l is None:
            return False # not exists
        if l != len(self.nums)-1:
            self.nums[l] = self.nums[-1]
            self.locs[self.nums[l]] = l
        self.nums.pop()
        del self.locs[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.nums) == 0:
            return False
        return self.nums[randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
assert obj.insert(1)
assert not obj.insert(1)
assert not obj.remove(2);
assert obj.insert(2)
assert obj.getRandom() in [1,2]
assert obj.remove(1);
assert obj.getRandom() == 2
assert obj.getRandom() == 2
