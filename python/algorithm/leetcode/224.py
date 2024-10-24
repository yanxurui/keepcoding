# https://leetcode.com/problems/basic-calculator/discuss/62377/16-ms-solution-in-C++-with-stacks/64056

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [] # stack of last operand
        num = 0 # last operand
        ops = [] # stack of last operator
        op = 1 # last operator
        rst = 0 # current result
        for i,c in enumerate(s):
            if c.isdigit():
                num = 10*num + int(c)
            elif c == '+':
                rst += num * op
                op = 1
                num = 0
            elif c == '-':
                rst += num * op
                op = -1
                num = 0
            elif c == '(':
                nums.append(rst)
                ops.append(op)
                rst = 0
                op = 1
                num = 0
            elif c == ')':
                rst += num * op
                rst = nums.pop() + rst * ops.pop()
                num = 0
            elif c == ' ':
                continue
            else:
                raise('Wrong input')
        rst += num*op
        return rst

# improved
class Solution2(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = [] # stack of last operand
        num = 0 # last operand
        ops = [] # stack of last operator
        op = 1 # last operator
        rst = 0 # current result
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                while i < len(s) and s[i].isdigit():
                    num = 10*num + int(s[i])
                    i += 1
                # end of a num, do the math
                rst += num * op
                num = 0
                continue
            elif c == '+':
                op = 1
            elif c == '-':
                op = -1
            elif c == '(':
                nums.append(rst)
                ops.append(op)
                rst = 0
                op = 1
                num = 0
            elif c == ')':
                rst = nums.pop() + rst * ops.pop()
                num = 0
            i += 1
        return rst


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('1 + 1'),
            2
        ),
        (
            (' 2-1 + 2 '),
            3
        ),
        (
            ('(1+(4+5+2)-3)+(6+8)'),
            23
        ),
        (
            ('(1-(1-2)'),
            2
        ),
        (
            ('1+23'),
            24
        ),
        (
            ('(1+1)-(1+1)'),
            0
        )
    ]
    test(Solution2().calculate, test_data)
