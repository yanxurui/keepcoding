from typing import List
from collections import defaultdict

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        rst = []
        stack = [(101, 0)] # decreasing
        for i in range(len(T)-1, -1, -1):
            t = T[i]
            while t >= stack[-1][0]:
                stack.pop()
            if stack[-1][0] == 101:
                rst.append(0)
            else:
                rst.append(stack[-1][1]-i)
            stack.append((t, i))
        return rst[::-1]


# https://leetcode.com/problems/daily-temperatures/discuss/109832/Java-Easy-AC-Solution-with-Stack

class Solution2:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        rst = [0] * len(T)
        stack = [] # decreasing
        for i in range(len(T)):
            t = T[i]
            while stack and t > T[stack[-1]]:
                idx = stack.pop()
                rst[idx] = i - idx
            stack.append(i)
        return rst



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0]
        ),
        (
            [89,62,70,58,47,47,46,76,100,70],
            [8,1,5,4,3,2,1,1,0,0]
        ),
    ]
    test(Solution2().dailyTemperatures, test_data)

