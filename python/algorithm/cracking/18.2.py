# -*- coding:utf-8 -*-

class NextElement:
    def findNext(self, A, n):
        # write code here
        stack = [-1] # decreasing
        rst = []
        for i in range(len(A)-1, -1, -1):
            while stack[-1] != -1 and stack[-1] <= A[i]:
                stack.pop()
            rst.append(stack[-1])
            stack.append(A[i])
        return rst[::-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [11,13,10,5,12,21,3],
                7
            ),
            [13,21,12,12,21,-1,-1]
        ),
        
    ]
    test(NextElement().findNext, test_data)
