# -*- coding:utf-8 -*-

class Count2:
    def countNumberOf2s(self, n):
        # write code here
        rst = 0
        m = 1
        while m <= n:
            a = n//m
            b = n%m
            # the current digit >2, =2, <2
            if a%10 > 2:
                rst += (a//10+1)*m
            elif a%10 == 2:
                rst += (a//10)*m + (b+1)
            else:
                rst += (a//10)*m
            m *= 10
        return rst


if __name__ == '__main__':
    from testfunc import test
    from common import TreeNode, ListNode
    test_data = [
        (
            10,
            1
        ),
        
    ]
    test(Count2().countNumberOf2s, test_data)
