class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for o in tokens:
            if o in ['+', '-', '*', '/']:
                op2 = stack.pop()
                op1 = stack.pop()
                if o == '+':
                    res = op1+op2
                elif o == '-':
                    res = op1-op2
                elif o == '*':
                    res = op1*op2
                elif o == '/':
                    res = op1 / op2
                    res = int(res)
                stack.append(res)
            else:
                stack.append(int(o))
        return stack.pop()        


if __name__ == '__main__':
    from testfunc import test
    from common import ListNode
    test_data = [
        (
            (["2", "1", "+", "3", "*"]),
            9
        ),
        (
            (["4", "13", "5", "/", "+"]),
            6
        ),
        (
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]),
            22
        )
    ]
    test(Solution().evalRPN, test_data)

