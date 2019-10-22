# -*- coding:utf-8 -*-
class Ants:
    def antsCollision(self, n):
        # write code here
        return 1 - 2.0/(2**n)


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            3,
            0.75
        )
    ]
    test(Ants().antsCollision, test_data)
