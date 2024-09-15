class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        op = '+'
        stack_num = []
        stack_op = []
        sign = 1
        last_c = ''
        for i, c in enumerate(s + '='):
            if c == ' ':
                continue
            if c == '(':
                stack_op.append(op)
                stack_op.append(len(stack_num))
                assert num == 0
                op = '+'
            elif c.isdigit():
                num = 10 * num + sign * int(c)
            else:
                # need some special handling for 2/-3
                if c == '-':
                    # - is sign only instead of op
                    if last_c == '*' or last_c == '/':
                        sign = -1
                        last_c = c
                        continue
                # end of a number
                # reset sign
                sign = 1
                # do the math
                if op == '+':
                    stack_num.append(num)
                elif op == '-':
                    stack_num.append(-num)
                elif op == '*':
                    stack_num.append(stack_num.pop() * num)
                elif op == '/':
                    stack_num.append(int(stack_num.pop() / num))
                num = 0
                
                if c == ')':
                    # reduce the value of the entire (xxx) into a single number
                    top = stack_op.pop()
                    op = stack_op.pop() # the op before (
                    while len(stack_num) > top:
                        last = stack_num.pop()
                        num += last
                elif c == '=':
                    break
                else:
                    assert c in set(['+', '-', '*', '/'])
                    op = c
            last_c = c
        return sum(stack_num)
                

if __name__ == '__main__':
    from testfunc import test
    from common import unordered_equal
    test_data = [  
        (
            "1+1",
            2
        ),
        (
            "6-4/2",
            4
        ),
        (
            "2*(5+5*2)/3+(6/2+8)",
            21
        ),
        (
            '5-3/2',
            4
        ),
        (
            '1-2-1',
            -2
        ),
        (
            '-1',
            -1
        ),
        (
            '2*-3',
            -6
        ),
        (
            '1-(-1)',
            2
        )
    ]
    test(Solution().calculate, test_data)
