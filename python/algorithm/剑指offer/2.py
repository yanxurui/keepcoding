# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        tmp = []
        for c in s:
            if c == ' ':
                tmp.append('%20')
            else:
                tmp.append(c)
        return ''.join(tmp)


# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('We Are Happy'),
            'We%20Are%20Happy'
        ),
        (
            ('  '),
            '%20%20'
        ),
        (
            (''),
            ''
        )
    ]
    test(Solution().replaceSpace, test_data)