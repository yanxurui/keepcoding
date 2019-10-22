class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '[':']', '{':'}'}
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not (stack and c == mapping[stack.pop()]):
                    return False
        return not stack


if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            '()',
            True
        ),
        (
            "()[]{}",
            True
        ),
        (
            "(]",
            False
        ),
        (
            "([)]",
            False
        ),
        (
            "{[]}",
            True
        ),
    ]
    test(Solution().isValid, test_data)

