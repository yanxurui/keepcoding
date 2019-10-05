class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack1 = []
        self._stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self._stack2:
            return self._stack2.pop()
        else:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
            return self._stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        x = self.pop()
        self._stack2.append(x)
        return x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self._stack1 or self._stack2)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


if __name__ == '__main__':
    queue = MyQueue()

    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() == False
