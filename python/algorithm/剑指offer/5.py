# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack2.append(node)

    def pop(self):
        # return xx
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        return self.stack1.pop()

# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

if __name__ == '__main__':
    q = Solution()
    q.push(1)
    q.push(2)
    assert q.pop() == 1
    q.push(3)
    assert q.pop() == 2
    assert q.pop() == 3
