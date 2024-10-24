# https://leetcode.com/problems/basic-calculator-ii/discuss/63003/Share-my-java-solution
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # rst op1 num op2
        num = 0
        nums = []
        op = '+' # last operator
        for c in s.replace(' ', '')+' ':
            if c.isdigit():
                num = 10*num + int(c)
            else:
                if op == '*':
                    nums.append(nums.pop() * num)
                if op == '/':
                    nums.append(int(nums.pop()/num))
                if op == '+':
                    nums.append(num)
                if op == '-':
                    nums.append(-1*num)
                num = 0
                if c == ' ':
                    continue
                op = c

        return sum(nums)


# https://leetcode.com/problems/basic-calculator-ii/discuss/63014/My-16-ms-No-stack-One-pass-short-C%2B%2B-solution
# no stack
class Solution2(object):
    def calculate(self, s):
        rst = 0
        cur = 0
        num = 0
        op = '+'
        n = len(s)
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                num = 10*num + int(c)
            else:
                cur = self.cal(cur, num, op)
                if c == '+' or c == '-':
                    rst += cur
                    cur = 0
                op = c
                num = 0
        rst += self.cal(cur, num, op)
        return rst
    def cal(self, num1, num2, op):
        if op == '+':
            return num1+num2
        elif op == '-':
            return num1-num2
        elif op == '*':
            return num1*num2
        elif op == '/':
            return int(num1/num2)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('3+2*2'),
            7
        ),
        (
            (' 3/2 '),
            1
        ),
        (
            (' 3+5 / 2 '),
            5
        ),
        (
            ("14-3/2"),
            13
        )
    ]
    test(Solution2().calculate, test_data)
