# -*- coding:utf-8 -*-

class Rank:
    def getRankOfNumber(self, A, n):
        # write code here
        nums = []
        rst = []
        for i in A:
            j = self.bs(nums, i)
            rst.append(j)
            if j == len(nums):
                nums.append(i)
            else:
                nums.insert(j, i)
        return rst
    def bs(self, nums, x):
        # find the first value that is >= x
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m] == x:
                return m
            elif x > nums[m]:
                l = m+1
            else:
                h = m-1
        return l


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,2,3,4,5,6,7],7
            ),
            [0,1,2,3,4,5,6]
        )
    ]
    test(Rank().getRankOfNumber, test_data)
