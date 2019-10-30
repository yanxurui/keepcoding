import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        s = 0
        for n in w:
            s += n
            self.w.append(s)

    def pickIndex(self) -> int:
        # binary search
        # find the index of the value that is >= x
        x = random.randint(1, self.w[-1])
        l = 0
        h = len(self.w) - 1
        while l <= h:
            m = (l+h)//2
            if self.w[m] == x:
                return m
            elif self.w[m] < x:
                l = m+1
            else:
                h = m-1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


