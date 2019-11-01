# https://leetcode.com/problems/tag-validator/discuss/103368/Java-Solution%3A-Use-startsWith-and-indexOf

UpperLetters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and len(stack) == 0:
                return False
            elif code.startswith('<![CDATA[', i):
                i = code.find(']]>', i+9)
                if i < 0:
                    return False
                i += 3
            elif code.startswith('</', i):
                j = code.find('>', i+2)
                if j < 0:
                    return False
                t = self.tagName(code, i+2, j)
                if t is False:
                    return False
                if len(stack) == 0 or stack.pop() != t:
                    return False
                i = j + 1
            elif code[i] == '<':
                j = code.find('>', i+1)
                if j < 0:
                    return False
                t = self.tagName(code, i+1, j)
                if t is False:
                    return False
                stack.append(t)
                i = j + 1
            else:
                i += 1
        return len(stack) == 0

    def tagName(self, code, i, j):
        if j-i == 0 or j-i > 9:
            return False
        for k in range(i, j):
            if code[k] not in UpperLetters:
                return False
        return code[i:j]



if __name__ == '__main__':
    from testfunc import test

    test_data = [  
        (
            '<DIV>This is the first line <![CDATA[<div>]]></DIV>',
            True
        ),
        (
            '<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>',
            True
        ),
        (
            '<A>  <B> </A>   </B>',
            False
        ),
        (
            '<DIV>  div tag is not closed  <DIV>',
            False
        ),
        (
            '<DIV>  unmatched <  </DIV>',
            False
        ),
        (
            '<DIV> closed tags with invalid tag name  <b>123</b> </DIV>',
            False
        ),
        (
            '<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>',
            False
        ),
        (
            '<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>',
            False
        ),
        (
            '<A></A>',
            True
        ),
        (
            '<A></A><B></B>',
            False
        ),
        
    ]
    test(Solution().isValid, test_data)

