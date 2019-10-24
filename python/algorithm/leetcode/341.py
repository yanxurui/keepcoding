# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, v):
        self.isInt = True
        if type(v) == list:
            self.isInt = False
        self.v = v

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.isInt

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInt:
            return self.v
        else:
            return None


    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInt:
            return None
        else:
            return self.v


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.l = nestedList # list type
        self.i = 0
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            v = self.l[self.i]
            self.i += 1
            return v.getInteger()
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        while True:
            while self.i == len(self.l):
                if self.stack:
                    self.l, self.i = self.stack.pop()
                    self.i += 1
                else:
                    return False

            v = self.l[self.i]
            if v.isInteger():
                return True
            else:
                self.stack.append((self.l, self.i))
                self.l = v.getList()
                self.i = 0
        return False


def build(v):
    if type(v) == int:
        return NestedInteger(v)
    else:
        rst = []
        for i in v:
            rst.append(build(i))
        return NestedInteger(rst)

def para(l):
    return [build(v) for v in l]




nestedList = para([[1,1],2,[1,1]])

# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())

assert v == [1,1,2,1,1]



nestedList = para([1,[4,[6]]])

# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())

assert v == [1,4,6]