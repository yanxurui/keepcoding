from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.pq = defaultdict(list)
        self.maxF = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxF:
            self.maxF = f
        self.pq[f].append(val)

    def pop(self) -> int:
        val = self.pq[self.maxF].pop()
        self.freq[val] = self.freq[val] - 1
        if len(self.pq[self.maxF]) == 0:
            self.maxF -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
