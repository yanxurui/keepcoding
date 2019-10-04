# -*- coding:utf-8 -*-
class Replacement:
    def replaceSpace(self, iniString, length):
        # write code here
        return '%20'.join(iniString.split(' '))

if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                'Mr John Smith',
                13
            ),
            'Mr%20John%20Smith'
        ),
        (
            (
                'Hello  World',
                12
            ),
            'Hello%20%20World'
        )
    ]
    test(Replacement().replaceSpace, test_data)
