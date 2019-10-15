# Below is the interface for Iterator, which is already defined for you.
#
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._nums = nums
        self._pos = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._pos < len(self._nums)


    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        if self.hasNext():
            v = self._nums[self._pos]
            self._pos += 1
            return v
        else:
            raise Exception()

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._cur = None # cache next element

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self._cur:
            self._cur = self.next()
        return self._cur

    def next(self):
        """
        :rtype: int
        """
        if self._cur:
            rst = self._cur
            self._cur = None
        else:
            if self.hasNext():
                rst = self._iterator.next()
            else:
                raise Exception()
        return rst

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self._cur else self._iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
nums = [1,2,3]
iter = PeekingIterator(Iterator(nums))

i = 0
while iter.hasNext():
    assert iter.peek() == nums[i]   # Get the next element but not advance the iterator.
    assert iter.next() == nums[i]   # Should return the same value as [val].
    i += 1



iter = PeekingIterator(Iterator(nums))


assert iter.next() == nums[0]
assert iter.peek() == nums[1]

assert iter.next() == nums[1]
assert iter.peek() == nums[2]
assert iter.peek() == nums[2]

assert iter.next() == nums[2]

