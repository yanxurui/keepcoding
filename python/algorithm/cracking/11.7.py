# -*- coding:utf-8 -*-

INT_MIN = -(1<<31)

class Stack:
    def getHeight(self, men, n):
        # write code here
        dp = [INT_MIN] # increasing
        for i in men:
            j = self.bs(dp, i)
            if j == len(dp):
                dp.append(i)
            else:
                dp[j] = i
        return len(dp)-1

    def bs(self, num, x):
        # find the first value that is >= x
        l = 0
        h = len(num)-1
        if x > num[h]:
            return h+1
        while l <= h:
            m = (l+h)//2
            if x == num[m]:
                return m
            elif x > num[m]:
                l = m+1
            else:
                h = m-1
        return l


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,6,2,5,3,4],
                6
            ),
            4
        )
    ]
    test(Stack().getHeight, test_data)
