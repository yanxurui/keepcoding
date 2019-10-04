
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
    test(Solution().calculate, test_data)
