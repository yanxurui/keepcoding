class Solution:
    def process(self, s):
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = self.process(s)
        stack2 = self.process(t)
        return stack1 == stack2
        
