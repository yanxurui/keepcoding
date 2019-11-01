class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.front = 0
        self.rear = -1
        self.q = [0] * self.size
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            self.rear += 1
            self.q[self.rear%self.size] = value
            return True
        else:
            return False

        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.front += 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.q[self.front%self.size]
        return -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.q[self.rear%self.size]
        return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front > self.rear
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.rear - self.front == self.size -1

        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(2)
assert obj.enQueue(1)
assert obj.enQueue(2)
assert obj.isFull()
assert obj.enQueue(3) == False
assert obj.Front() == 1
assert obj.Rear() == 2
assert obj.deQueue()
assert obj.isEmpty() == False
assert obj.deQueue()
assert obj.isEmpty()
