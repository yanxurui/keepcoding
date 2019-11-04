# https://leetcode.com/problems/online-stock-span/discuss/168311/C%2B%2BJavaPython-O(1)

class StockSpanner:

    def __init__(self):
        self.stack = [] # decreasing

    def next(self, price: int) -> int:
        rst = 1
        while self.stack and price >= self.stack[-1][0]:
            rst += self.stack.pop()[1]
        self.stack.append((price, rst))
        return rst


# Your StockSpanner object will be instantiated and called as such:
S = StockSpanner()
assert S.next(100) == 1
assert S.next(80) == 1
assert S.next(60) == 1
assert S.next(70) == 2
assert S.next(60) == 1
assert S.next(75) == 4
assert S.next(85) == 6
