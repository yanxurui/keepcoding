# -*- coding:utf-8 -*-
from collections import deque

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class CatDogAsylum:
    def insert(self, val):
        n = ListNode(val)
        self.tail.next = n
        n.prev = self.tail
        self.tail = n
        return n
    def delete(self, p):
        p.prev.next = p.next
        if p == self.tail:
            self.tail = p.prev
        else:
            p.next.prev = p.prev
        return p.val

    def asylum(self, ope):
        self.head = self.tail = LinkedList(0)
        # write code here
        dog = deque()
        cat = deque()
        rst = []
        for op in ope:
            if op[0] == 1:
                if op[1] > 0:
                    dog.append(self.insert(op[1]))
                elif op[1] < 0:
                    cat.append(self.insert(op[1]))
            elif op[0] == 2:
                if op[1] == 0:
                    if self.head != self.tail:
                        v = self.delete(self.head.next)
                        rst.append(v)
                        if v > 0:
                            dog.popleft()
                        else:
                            cat.popleft()
                elif op[1] == 1:
                    if dog:
                        rst.append(self.delete(dog.popleft()))
                elif op[1] == -1:
                    if cat:
                        rst.append(self.delete(cat.popleft()))
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            [[1,1],[1,-1],[2,0],[2,-1]],
            [1,-1]
        ),
        (
            [[1,-5],[1,-1],[1,9],[1,9],[2,0],[2,1],[1,-8],[2,1],[1,-71],[1,-92],[1,18],[1,91],[1,61],[2,-1],[1,-35],[1,95],[1,-49],[1,9],[1,78],[2,0],[1,91],[1,-96],[2,-1],[2,0],[2,-1],[2,1],[1,38],[2,0],[1,45],[2,0],[1,-51],[2,1],[2,1],[2,-1],[1,39],[1,59],[1,45],[2,0],[1,-70],[2,0],[1,23],[1,88],[1,83],[1,69],[1,-78],[1,-3],[1,-9],[1,-20],[1,-74],[1,-62],[1,5],[1,55],[1,-36],[1,-21],[1,-94],[1,-27],[1,-69],[2,0],[1,-30],[1,-84],[2,0],[2,0],[2,-1],[1,92],[1,60],[2,1],[2,0],[1,-63],[2,0],[1,-87],[1,66],[2,0],[1,17],[2,0],[2,1],[1,-41],[1,-3],[1,-29],[1,72],[2,1],[1,35],[1,81],[1,-83],[1,-17],[1,36],[1,99],[1,-17],[1,8],[2,0],[1,80],[1,50],[1,80],[2,0],[1,-48],[1,-82],[1,-63],[1,2],[2,1],[1,-43],[1,59],[1,93],[1,55],[1,-93],[2,-1],[1,2],[1,13],[2,0]],
            [-5,9,9,-1,-8,-71,-92,-35,18,91,61,95,9,-49,78,91,-96,38,45,-51,39,59,45,-70,23,88,83,69,-78,5,-3,-9]
        ),
    ]
    test(CatDogAsylum().asylum, test_data)

