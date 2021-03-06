# https://leetcode.com/problems/implement-stack-using-queues/discuss/62527/A-simple-C%2B%2B-solution

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self._queue.append(x)
        for i in range(len(self._queue)-1):
            self._queue.append(self._queue.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._queue.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self._queue else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == '__main__':
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() == False
