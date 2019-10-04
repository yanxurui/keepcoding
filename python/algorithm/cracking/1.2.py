# -*- coding:utf-8 -*-
class Reverse:
    def reverseString(self, iniString):
        # write code here
        iniString = list(iniString)
        n = len(iniString)
        for i in range(n//2):
            tmp = iniString[i]
            iniString[i] = iniString[n-1-i]
            iniString[n-1-i] = tmp
        return ''.join(iniString)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('This is nowcoder'),
            "redocwon si sihT"
        ),
        (
            (''),
            ''
        )
    ]
    test(Reverse().reverseString, test_data)
