# -*- coding:utf-8 -*-
class Different:
    def checkDifferent(self, iniString):
        # write code here
        s = sorted(list(iniString))
        for i in range(1, len(s)):
        	if s[i] == s[i-1]:
        		return False
       	return True


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('aeiou'),
            True
        ),
        (
            ('BarackObama'),
            False
        )
    ]
    test(Different().checkDifferent, test_data)
