# -*- coding:utf-8 -*-
class KthNumber:
    def findKth(self, k):
        # write code here
        l = [1]
        i3 = i5 = i7 = 0
        for i in range(k):
            n = min(3*l[i3], 5*l[i5], 7*l[i7])
            l.append(n)
            if n == 3*l[i3]:
                i3 += 1
            if n == 5*l[i5]:
                i5 += 1
            if n == 7*l[i7]:
                i7 += 1
        return l[-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            3,
            7
        ),
        (
            4,
            9
        )
    ]
    test(KthNumber().findKth, test_data)
