class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i,c in enumerate(s):
            if c == ')' and stack and s[stack[-1]]=='(':
                stack.pop()
            else:
                stack.append(i)
        stack.insert(0, -1)
        stack.append(len(s))
        longest = 0
        for j in range(1, len(stack)):
            l = stack[j] - stack[j-1]
            if l > longest:
                longest = l
        return longest - 1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            '(()',
            2
        ),
        (
            ')()())',
            4
        ),
        (
            '(',
            0
        ),
        (
            '',
            0
        )
    ]
    test(Solution().longestValidParentheses, test_data)
