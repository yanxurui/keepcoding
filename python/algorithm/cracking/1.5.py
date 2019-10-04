# -*- coding:utf-8 -*-
class Zipper:
    def zipString(self, iniString):
        # write code here
        chars = []
        prev = None
        for c in iniString:
            if c == prev:
                chars[-1][1] += 1
            else:
                chars.append([c, 1])
                prev = c

        res = ''.join([char + str(count) for char,count in chars])
        return res if len(res) < len(iniString) else iniString



if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            ('aabcccccaaa'),
            'a2b1c5a3'
        ),
        (
            ('welcometonowcoderrrrr'),
            'welcometonowcoderrrrr'
        )
    ]
    test(Zipper().zipString, test_data)
