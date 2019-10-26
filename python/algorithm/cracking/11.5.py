# -*- coding:utf-8 -*-

class Finder:
    def findString(self, s, n, x):
        # write code here
        l = 0
        h = n-1
        while l <= h:
            m = (l+h)//2
            old = m
            while s[m] == '' and m >= l:
                m -= 1
            if m < l:
                l = old+1
            else:
                if x == s[m]:
                    return m
                elif x < s[m]:
                    h = m-1
                else:
                    l = m+1
        return -1


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                ["a","b","","c","","d"],6,"c"
            ),
            3
        )
    ]
    test(Finder().findString, test_data)
