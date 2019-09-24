# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48808/My-pretty-simple-code-to-solve-it
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = None
        self._min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self._stack:
            self._stack.append((x, min(x, self._stack[-1][1])))
        else:
            self._stack = [(x, x)]


    def pop(self):
        """
        :rtype: None
        """
        self._stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._stack[-1][1]

        
if __name__ == '__main__':
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    assert minStack.getMin() == -3
    minStack.pop();
    assert minStack.top() == 0
    assert minStack.getMin() == -2

