# https://leetcode.com/problems/my-calendar-i/discuss/109476/Binary-Search-Tree-python

class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root:
            return self.util(start, end, self.root)
        else:
            self.root = Node(start, end)
            return True
    def util(self, start, end, root):
        if start >= root.e:
            if root.right:
                return self.util(start, end, root.right)
            else:
                root.right = Node(start, end)
                return True
        elif end <= root.s:
            if root.left:
                return self.util(start, end, root.left)
            else:
                root.left = Node(start, end)
                return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
assert obj.book(10, 20)
assert obj.book(15, 25) is False
assert obj.book(20, 30)


