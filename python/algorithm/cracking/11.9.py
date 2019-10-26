# -*- coding:utf-8 -*-

class AntiOrder:
    def count(self, A, n):
        # write code here
        nums = []
        rst = 0
        for i in A:
            j = self.bs(nums, i)
            rst += (len(nums)-j)
            if j == len(nums):
                nums.append(i)
            else:
                nums.insert(j, i)
        return rst

    def bs(self, nums, x):
        # find the index of the first value that is > x
        l = 0
        h = len(nums)-1
        while l <= h:
            m = (l+h)//2
            if x >= nums[m]:
                l = m+1
            else:
                h = m-1
        return l


if __name__ == '__main__':
    from testfunc import test
    test_data = [
        (
            (
                [1,2,3,4,5,6,7,0],8
            ),
            7
        )
    ]
    test(AntiOrder().count, test_data)
