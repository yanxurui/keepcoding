# -*- coding:utf-8 -*-
class Permutation:
    # A是一个字符串
    def getPermutation(self, A):
        # write code here
        if not A:
            return ['']
        rst = []
        for i in range(len(A)):
            for p in self.getPermutation(A[:i]+A[i+1:]):
                rst.append(A[i]+p)
        rst.sort()
        return rst[::-1]


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            'ABC',
            ["CBA","CAB","BCA","BAC","ACB","ABC"]
        )
    ]
    test(Permutation().getPermutation, test_data)
